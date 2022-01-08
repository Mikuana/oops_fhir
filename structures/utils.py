from typing import List, Dict
from importlib import import_module
import builtins
import keyword
import re
import textwrap
from typing import Union

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
