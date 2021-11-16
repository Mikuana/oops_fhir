import json
import keyword
import re
import subprocess
import sys
import tempfile
import textwrap
import zipfile
from enum import Enum
from importlib import import_module
from pathlib import Path
from typing import Tuple, List, Any, Union
from urllib.request import urlretrieve

from fhir.resources.codesystem import CodeSystem

reg_p = Path(Path(__file__).parent, "../oops_fhir/terminologies/registry.json")
registry = json.loads(reg_p.read_text())

d = Path(__file__).parent

_class_case_pattern = re.compile(r'[^a-zA-Z0-9]')


def wrap(indent: int, text: Union[str, None]):
    return (chr(10) + ' ' * indent).join([l for l in textwrap.wrap(text or '')])


def class_case(x: str):
    y = _class_case_pattern.sub('', x.title())
    if keyword.iskeyword(y):
        return f"x{y}"
    elif str(y[0]).isdigit():
        return f"x{y}"
    else:
        return y


def snake_case(x: str):
    y = re.sub(r"(?<!^)(?<![A-Z])(?=[A-Z])", "_", x).lower()
    y = re.sub(r"[^a-z0-9_]", "_", y)
    y = re.sub(r"_{2,}", "_", y)
    y = y if y[0].isalpha() else f"x{y}"
    return y


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
            Path(__file__).parent, "../oops_fhir/terminologies/r4/code_system",
            snake_case(r.name)
        )
        self.target.parent.mkdir(parents=True, exist_ok=True)
        Path(self.target.parent, '__init__.py').touch()
        txt = textwrap.dedent(f'''
        """
        {r.title} ({r.status})

        {r.description}

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


if __name__ == "__main__":
    # R4
    d = Path("r4")
    j = json.loads(Path(d, 'valuesets.json').read_text())
    for e in j['entry']:
        if e['resource']['resourceType'] == 'CodeSystem':
            # if e['resource']['id'] == 'standards-status':
            print(e['resource']['name'])
            rf = CodeSystemFactory(e['resource'])

    # ValueSet(f"{prefix}/r4/value_set/administrative_gender.json")
    # reg_p.write_text(
    #     json.dumps({k: registry[k] for k in sorted(registry.keys())}, indent=2)
    # )
