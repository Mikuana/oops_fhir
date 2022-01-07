import sys
import subprocess
import json
import re
import textwrap
from pathlib import Path
from typing import Union

from fhir.resources.bundle import Bundle

_class_case_pattern = re.compile(r"[^a-zA-Z0-9]")


def wrap(indent: int, text: Union[str, None]):
    return (chr(10) + " " * indent).join([i for i in textwrap.wrap(text or "")])


import re
import keyword

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


def safe_first(x: str):
    # make first character safe
    if re.match(r"[^a-zA-Z]", x[0]):
        x = rep.get(x[0], "unknown") + x[1:]
    return x


var_pat = re.compile(r"[^a-z0-9_]", re.IGNORECASE)
extra_under_pat = re.compile(r"_{2,}")
camel_break_pat = re.compile(r"(?<!^)(?<![A-Z])(?=[A-Z])")


def snake_case(x: str):
    x = safe_first(x)
    x = var_pat.sub("_", x)
    x = camel_break_pat.sub("_", x).lower()
    x = extra_under_pat.sub("_", x)
    x = x.strip("_")

    if keyword.iskeyword(x):
        return f"v_{x}"
    else:
        return x


class_pat = re.compile(r"[^a-zA-Z0-9]")


def class_case(x: str):
    x = safe_first(x)
    x = class_pat.sub("", x.title())

    if keyword.iskeyword(x):
        return f"v{x}"
    else:
        return x


registry = {}

bp = Path("/home/chris/PycharmProjects/oops_fhir/structures/")
p2 = Path("/home/chris/PycharmProjects/oops_fhir/oops_fhir")

sources = [("r4",), ("us", "core")]
for source in sources:
    sp = Path(p2, *source)
    sp.mkdir(exist_ok=True, parents=True)
    Path(sp, "__init__.py").touch()
    bundle: Union[Bundle, None] = None
    resources = []
    for bj in Path(bp, *source).glob("*.json"):
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
            resource.text = None
            rtp = Path(sp, snake_case(resource.resource_type))
            rtp.mkdir(exist_ok=True)
            Path(rtp, "__init__.py").touch()

            rp = Path(rtp, snake_case(resource.name))
            rp.with_suffix(".json").write_text(
                json.dumps(json.loads(resource.json()), indent=2)
            )

            rp.with_suffix(".py").write_text(
                textwrap.dedent(
                    f'''
                """
                {resource.name}

                {resource.description}

                {resource.url}
                """

                from pathlib import Path

                from fhir.resources.{resource.resource_type.lower()} import {resource.resource_type}

                resource = {resource.resource_type}.parse_file(Path(__file__).with_suffix('.json'))
                '''
                )
            )
            # subprocess.check_call(
            #     [sys.executable, "-m", "black", "-q", rp.with_suffix('.py')]
            # )

            registry[resource.url] = (
                rp.relative_to("/home/chris/PycharmProjects/oops_fhir/")
                .as_posix()
                .replace("/", ".")
            )

reg_p = Path("/home/chris/PycharmProjects/oops_fhir/oops_fhir/registry.json")
reg_p.write_text(
    json.dumps({k: registry[k] for k in sorted(registry.keys())}, indent=2)
)
