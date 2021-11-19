import json
import re
import subprocess
import sys
import tempfile
import textwrap
import zipfile
from importlib import import_module
from pathlib import Path
from typing import Tuple, List, Union
from urllib.request import urlretrieve

from fhir.resources.codesystem import CodeSystem
from fhir.resources.valueset import ValueSet

reg_p = Path(Path(__file__).parent, "../oops_fhir/registry.json")
registry = json.loads(reg_p.read_text())

d = Path(__file__).parent

_class_case_pattern = re.compile(r'[^a-zA-Z0-9]')


def wrap(indent: int, text: Union[str, None]):
    return (chr(10) + ' ' * indent).join([l for l in textwrap.wrap(text or '')])


import re
import keyword

rep = {
    " ": "space",
    "!": "exclamation mark",
    "\"": "quotation mark",
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
    if re.match(r'[^a-zA-Z]', x[0]):
        x = rep.get(x[0], 'unknown') + x[1:]
    return x


var_pat = re.compile(r'[^a-z0-9_]', re.IGNORECASE)
extra_under_pat = re.compile(r'_{2,}')
camel_break_pat = re.compile(r"(?<!^)(?<![A-Z])(?=[A-Z])")


def snake_case(x: str):
    x = safe_first(x)
    x = var_pat.sub('_', x)
    x = camel_break_pat.sub('_', x).lower()
    x = extra_under_pat.sub('_', x)
    x = x.strip('_')

    if keyword.iskeyword(x):
        return f"v_{x}"
    else:
        return x


class_pat = re.compile(r'[^a-zA-Z0-9]')


def class_case(x: str):
    x = safe_first(x)
    x = class_pat.sub('', x.title())

    if keyword.iskeyword(x):
        return f"v{x}"
    else:
        return x


def prep_r4():
    url = 'http://hl7.org/fhir/definitions.json.zip'
    with tempfile.NamedTemporaryFile('wb') as tf:
        urlretrieve(url, tf.name)
        with zipfile.ZipFile(tf.name, 'r') as zip_ref:
            zip_ref.extractall(Path(d, 'r4'))


m = {
    'CodeSystem': CodeSystem
}


class CodeSystemFactory:
    def __init__(self, definition):
        r: CodeSystem = CodeSystem.parse_obj(definition)
        self.target = Path(
            Path(__file__).parent.parent, "oops_fhir/terminologies/r4/code_system",
            snake_case(r.name)
        )
        self.target.parent.mkdir(parents=True, exist_ok=True)
        Path(self.target.parent, '__init__.py').touch()
        txt = textwrap.dedent(f'''
        """
        {r.title} ({r.status})

        {wrap(8, r.description)}

        {r.url}
        """

        import json
        from pathlib import Path

        from fhir.resources.codesystem import CodeSystem
        from oops_fhir.terminologies import CodeSystemConceptFrame

        __all__ = {[class_case(x.display or x.code) for x in r.concept or ()]}

        _resource = CodeSystem.parse_file(Path(__file__).with_suffix('.json'))
        ''')

        for ix, con in enumerate(r.concept or ()):
            txt += textwrap.dedent(f'''
            class {class_case(con.display or con.code)}(CodeSystemConceptFrame):
                """
                {wrap(16, con.display)}

                {wrap(16, con.definition)}
                """
                resource = _resource.concept[{ix}]
            ''')

        Path(self.target).with_suffix('.py').write_text(txt)
        Path(self.target).with_suffix('.json').write_text(
            json.dumps(definition, indent=2)
        )
        subprocess.check_call(
            [sys.executable, "-m", "black", "-q", self.target.with_suffix('.py')]
        )
        self.resource = r


class ValueSetFactory:
    def __init__(self, definition):
        r: ValueSet = ValueSet.parse_obj(definition)
        self.target = Path(
            Path(__file__).parent.parent, "oops_fhir/terminologies/r4/value_set",
            snake_case(r.name)
        )
        self.target.parent.mkdir(parents=True, exist_ok=True)
        Path(self.target.parent, '__init__.py').touch()
        txt = textwrap.dedent(f'''
        """
        {r.title} ({r.status})

        {wrap(8, r.description)}

        {r.url}
        """

        from pathlib import Path

        from fhir.resources.valueset import ValueSet

        from oops_fhir.terminologies import ValueSetComposeFrame
        <import placeholder>

        _resource = ValueSet.parse_file(Path(__file__).with_suffix('.json'))
        ''')

        imports: List[Tuple[int, str]] = []
        for ix, inc in enumerate(r.compose.include or ()):
            if inc.concept:
                for ix2, con in enumerate(inc.concept):
                    txt += textwrap.dedent(f'''
                    class {class_case(con.display or con.code)}(ValueSetComposeFrame):
                        """
                        {wrap(24, con.display)}

                        {wrap(24, con.code)}
                        """
                        resource = _resource.compose.include[{ix}].concept[{ix2}]
                    ''')
            else:
                ref = registry.get(inc.system)
                if ref:
                    imports.append((ix, registry[inc.system]))
                    module = import_module(registry[inc.system])
                    for v in getattr(module, '__all__'):
                        txt += textwrap.dedent(f"""
                        {snake_case(getattr(module, v).resource.code)} = i{ix}.{v}
                        """)

        txt = txt.replace(
            '<import placeholder>',
            '\n'.join(f'import {x} as i{str(ix)}' for ix, x in imports)
        )

        Path(self.target).with_suffix('.py').write_text(txt)
        Path(self.target).with_suffix('.json').write_text(
            json.dumps(definition, indent=2)
        )
        subprocess.check_call(
            [sys.executable, "-m", "black", "-q", self.target.with_suffix('.py')]
        )
        self.resource = r


if __name__ == "__main__":
    d = Path("r4")
    j = json.loads(Path(d, 'valuesets.json').read_text())
    for e in j['entry']:
        if e['resource']['resourceType'] == 'CodeSystem':  # and e['resource']['name'] == 'AdministrativeGender':
            rf = CodeSystemFactory(e['resource'])
            print(rf.resource.name)
            registry[rf.resource.url] = rf.target.relative_to(
                Path(__file__).parent.parent.absolute()
            ).as_posix().replace('/', '.')

    for e in j['entry']:
        if e['resource']['resourceType'] == 'ValueSet':  # and e['resource']['name'] == 'AdministrativeGender':
            rf = ValueSetFactory(e['resource'])
            print(rf.resource.name)
            registry[rf.resource.url] = rf.target.relative_to(
                Path(__file__).parent.parent.absolute()
            ).as_posix().replace('/', '.')

    reg_p.write_text(json.dumps(registry, indent=2))
