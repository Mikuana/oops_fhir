import builtins
import json
import keyword
import logging
import re
import textwrap
from importlib import import_module
from pathlib import Path
from typing import List, Dict, Tuple
from typing import Union

from fhir.resources.bundle import Bundle
from fhir.resources.valueset import ValueSet

rep = {
    " ": "space",
    "!": "exclamation mark",
    '"': "quotation mark",
    "#": "number sign",
    "$": "dollar sign",
    "%": "percent sign",
    "&": "ampersand",
    "'": "apostrophe",
    "(": "left parenthesis",
    ")": "right parenthesis",
    "*": "asterisk",
    "+": "plus sign",
    ",": "comma",
    "-": "hyphen",
    ".": "period",
    "/": "slash",
    ":": "colon",
    ";": "semicolon",
    "<": "less than",
    "=": "equals to",
    ">": "greater than",
    "?": "question mark",
    "@": "at sign",
    "[": "left square bracket",
    "\\": "backslash",
    "]": "right square bracket",
    "^": "caret",
    "_": "underscore",
    "`": "grave accent",
    "{": "left curly brace",
    "|": "vertical bar",
    "}": "right curly brace",
    "~": "tilde",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero",
}

_class_case_pattern = re.compile(r"[^a-zA-Z0-9]")
class_pat = re.compile(r"[^a-zA-Z0-9]")
var_pat = re.compile(r"[^a-z0-9_]", re.IGNORECASE)
extra_under_pat = re.compile(r"_{2,}")
camel_break_pat = re.compile(r"(?<!^)(?<![A-Z])(?=[A-Z])")


def wrap(indent: int, text: Union[str, None]):
    return (chr(10) + " " * indent).join([i for i in textwrap.wrap(text or "")])


def safe_first(x: str):
    # make first character safe
    if re.match(r"[^a-zA-Z]", x[0]):
        x = rep.get(x[0], "unknown") + x[1:]
    return x


def snake_case(x: str):
    x = safe_first(x)
    x = var_pat.sub("_", x)
    x = camel_break_pat.sub("_", x).lower()
    x = extra_under_pat.sub("_", x)
    x = x.strip("_")

    if keyword.iskeyword(x) or x in dir(builtins):
        return f"{x}_"
    else:
        return x


def screaming_snake_case(x: str):
    # TODO: put in code system templates
    return snake_case(x).upper()


def camel_case(x: str):
    x = safe_first(x)
    x = class_pat.sub("", x)

    if keyword.iskeyword(x) or x in dir(builtins):
        return f"{x}_"
    else:
        return x


def all_imps(module: str) -> List[str]:
    return getattr(import_module(module), "__all__", [])


def namespace_imps(imps: List[str], space_index: int) -> Dict[str, str]:
    return {x: x + '_' + str(space_index) for x in imps}


def register_urls(sources: List[Tuple[str]]):
    registry = {}  # TODO: add optional read and overwrite
    reg_p = Path("/home/chris/PycharmProjects/oops_fhir/oops_fhir/registry.json")
    bp = Path("/home/chris/PycharmProjects/oops_fhir/structures/")
    p2 = Path("/home/chris/PycharmProjects/oops_fhir/oops_fhir")

    for source in sources:
        sp = Path(p2, *source)
        sp.mkdir(exist_ok=True, parents=True)
        Path(sp, "__init__.py").touch()
        bundle: Union[Bundle, None] = None
        resources = []
        for bj in Path(bp, *source).glob("*.json"):
            # if bj.name != 'valuesets.json':  # TODO: remove this skip
            #     continue
            try:
                print(bj)
                bundle = Bundle.parse_file(bj)
            except Exception as e:
                j = json.loads(bj.read_text())
                resource_type = j.get("resourceType")
                print(bj.name, resource_type)
                if resource_type == "ImplementationGuide" or bj.name == 'v2-tables.json':
                    continue
                elif resource_type:
                    from importlib import import_module

                    module = import_module(f"fhir.resources.{resource_type.lower()}")
                    resources.append(getattr(module, resource_type).parse_file(bj))
                else:
                    print(f"failed on parse: {bj}")
                    continue

            if bundle:
                # noinspection PyUnresolvedReferences
                resources = [e.resource for e in bundle.entry]

            for resource in resources:
                rtp = Path(sp, snake_case(resource.resource_type))
                rp = Path(rtp, snake_case(resource.name))
                registry[resource.url] = (
                    rp.relative_to("/home/chris/PycharmProjects/oops_fhir/")
                        .as_posix()
                        .replace("/", ".")
                )
    reg_p.write_text(json.dumps(
        {k: registry[k] for k in sorted(registry.keys())}, indent=2
    ))

    return registry


# noinspection PyUnresolvedReferences
class ValueSetStager:
    def __init__(self, value_set: ValueSet, registry: dict):
        self.passthrough = None
        self.resource = value_set
        self.concepts = dict()
        self.systems = dict()
        self.imports = dict()
        self.namespaces = 0

        if self.resource.expansion:
            self.concepts = {
                snake_case(v.code): v
                for v in self.resource.expansion.contains
            }

        else:
            for i in self.resource.compose.include:
                if i.concept:
                    self.systems[i.system] = {
                        snake_case(x.code): x for x in i.concept
                    }
                    self.namespaces += 1
                else:  # import module
                    try:
                        ref = registry[i.system]
                        imps = {'original': all_imps(ref)}
                        imps['aliases'] = [
                            f'{x}_' if x == camel_case(self.resource.name)
                            else x for x in imps['original']
                        ]
                        imps['statement'] = [
                            f'{k} as {v}'
                            if k != v else k for k, v in
                            dict(zip(imps['original'], imps['aliases'])).items()
                        ]
                        self.imports[import_module(ref)] = imps
                        self.namespaces += 1
                    except KeyError:
                        logging.warning(
                            f'ValueSet {self.resource.name} failed to import '
                            f'system reference {i.system}'
                        )

        if self.namespaces == 1 and self.imports:
            aliases = list(self.imports.values())[0]['aliases']
            if len(aliases) == 1:
                self.passthrough = aliases[0]


def stage_values(value_set, registry) -> ValueSetStager:
    x = ValueSetStager(value_set, registry)
    return x


def json_to_py(x: str):
    return json.loads(x)
