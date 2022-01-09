import json
from collections import Counter
from pathlib import Path
from typing import List, Dict, Tuple
from importlib import import_module
import builtins
import keyword
import re
import textwrap
from typing import Union

from fhir.resources.bundle import Bundle
from fhir.resources.valueset import ValueSet, ValueSetComposeIncludeConcept

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
        return f"v_{x}"
    else:
        return x


def class_case(x: str):
    x = safe_first(x)
    x = class_pat.sub("", x.title())

    if keyword.iskeyword(x) or x in dir(builtins):
        return f"v{x}"
    else:
        return x


def all_imps(module: str) -> List[str]:
    return getattr(import_module(module), "__all__")


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


def value_set_concepts(x: ValueSet) -> Dict[str, ValueSetComposeIncludeConcept]:
    if x.expansion:
        # noinspection PyUnresolvedReferences
        return {
            snake_case(v.code): v
            for v in x.expansion.contains
        }

    concepts = []
    for inclusion in x.compose.include:
        if inclusion.concept:
            concepts.append({
                snake_case(v.code): v
                for v in inclusion.concept
            })
        else:
            inclusion.system

    if len(concepts) == 1:
        concepts = concepts[0]
    else:
        merged_concepts = dict()
        names = Counter([snake_case(e) for s in concepts for e in s])
        dup_names = [k for k, v in names.items() if v > 1]
        print(dup_names)
        for ix, inclusion in enumerate(concepts):
            merged_concepts.update({
                f'{k}_{str(ix)}' if k in dup_names else k: v
                for k, v in inclusion.items()
            })

        concepts = merged_concepts

    return concepts


if __name__ == '__main__':
    v1 = ValueSet.parse_file(
        Path('/home/chris/PycharmProjects/oops_fhir/oops_fhir/r4/value_set/common_ucum_units.json'))
    v2 = ValueSet.parse_file('/home/chris/PycharmProjects/oops_fhir/oops_fhir/r4/value_set/yes_no_don_t_know.json')
    print(value_set_concepts(v1))
