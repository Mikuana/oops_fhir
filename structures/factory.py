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
from typing import Tuple, List, Any
from urllib.request import urlretrieve

reg_p = Path(Path(__file__).parent, "../oops_fhir/terminologies/registry.json")
registry = json.loads(reg_p.read_text())

d = Path(__file__).parent


def prep_r4():
    url = 'http://hl7.org/fhir/definitions.json.zip'
    with tempfile.NamedTemporaryFile('wb') as tf:
        urlretrieve(url, tf.name)
        with zipfile.ZipFile(tf.name, 'r') as zip_ref:
            zip_ref.extractall(Path(d, 'r4'))


class ResourceType(Enum):
    CODE_SYSTEM = "code_system"
    VALUE_SET = "value_set"


class ResourceMeta:
    raw_json: str
    """ Raw JSON string which defines the resource """

    definition: dict
    """ Dictionary object parsed from raw JSON string """

    target: Path
    """ Target python script for the resource """

    location: str
    """ A resource location identifier """

    url: str
    """ Resolvable URL to resource type definition """

    resource_type: ResourceType
    """ Type of FHIR resource that this frame will support """

    attribute_map = {
        "resourceType": "resource_type",
        "id": "id",
        "url": "url",
        "identifier": "identifier",
        "version": "version",
        "name": "name",
        "title": "title",
        "status": "status",
        "date": "date",
        "publisher": "publisher",
        "contact": "contact",
        "jurisdiction": "jurisdiction",
        "copyright": "copyright",
    }
    """
    A dictionary with expected keys to be mapped to variables, and values of
    the variable name to be assigned to.
    """


class ResourceFrame:
    imports: set = set()

    class Meta(ResourceMeta):
        pass

    def __init__(self, definition):
        pd = Path(Path(__file__).parent, "../oops_fhir/terminologies/r4", self.Meta.resource_type.value)

        self.Meta.definition = definition
        self.__doc__ = self.Meta.definition.get("description")
        self.Meta.url = self.Meta.definition["url"]

        self.Meta.target = Path(
            Path(pd, self.Meta.definition.get("id").replace("-", "_"))
        ).with_suffix(".py")
        self.Meta.location = (
            self.Meta.target.relative_to(Path(__file__).parent)
                .with_suffix("")
                .as_posix()
                .replace("/", ".")
        )

        self.pythonize()
        self.register()

    def expand_meta(self) -> List[Tuple[str, Any]]:
        em = []
        for k, v in self.Meta.attribute_map.items():
            if self.Meta.definition.get(k) is None:
                continue
            elif isinstance(self.Meta.definition.get(k), str):
                v2 = self.Meta.definition.get(k)
                v2 = "\n".join(textwrap.wrap(v2, 88))

                v2 = f'"""{v2}"""' if "\n" in v2 else f'"{v2}"'
            else:
                v2 = str(self.Meta.definition.get(k))

            em.append((f"_{v}_", v2))
        return em

    def concepts(self):
        ev: List[Tuple[str, str, dict]] = []
        for i in self.Meta.definition["compose"]["include"]:
            for j in i.get("concept", ()):
                d = {
                    "system": i["system"],
                    "code": j["code"],
                    "display": j.get("display"),
                }

                k = str(j.get("display", j.get("code")))
                k = re.sub(r"(?<!^)(?<![A-Z])(?=[A-Z])", "_", k).lower()
                k = re.sub(r"[^a-z0-9_]", "_", k)
                k = re.sub(r"_{2,}", "_", k)
                k = k if k[0].isalpha() else f"x{k}"

                vd = dict(url=self.Meta.url)
                if len(self.Meta.definition["compose"]["include"]) > 1:
                    vd["valueCoding"] = {a: b for a, b in d.items() if b}
                elif d.get("display"):
                    vd["valueString"] = d.get("display")
                else:
                    vd["valueCode"] = d.get("code")

                ev.append((k, j.get("display", j.get("code")), vd))
        return ev

    def pythonize(self):
        self.Meta.target.parent.mkdir(parents=True, exist_ok=True)
        Path(self.Meta.target.parent, '__init__.py').touch()
        concepts = self.concepts()
        values = [
            f"{name} = {value}\n" + (f'""" {desc} """\n' if desc else "")
            for name, desc, value in concepts
        ]
        all_values = [name for name, _, _ in concepts]
        self.Meta.target.write_text(
            '"""'
            + "\n".join(textwrap.wrap(self.__doc__ or '', 72))
            + '"""\n\n'
            + "\n".join(
                [
                    f"from {x.rsplit('.', 1)[0]} import {x.rsplit('.', 1)[1]}"
                    for x in self.imports
                ]
            )
            + f"\n__all__ = ["
            + ",".join(f"'{x}'" for x in all_values)
            + "]\n\n"
            + "\n".join(f"{n} = {v}" for n, v in self.expand_meta())
            + "\n\n"
            + "\n".join(values)
        )
        subprocess.check_call(
            [sys.executable, "-m", "black", "-q", self.Meta.target.as_posix()]
        )

    def register(self):
        registry[self.Meta.url] = self.Meta.target


class CodeSystem(ResourceFrame):
    class Meta(ResourceMeta):
        resource_type = ResourceType.CODE_SYSTEM

    def concepts(self):
        ev: List[Tuple[str, str, dict]] = []
        for j in self.Meta.definition.get("concept", ()):
            d = {
                "code": j["code"],
                "display": j.get("display"),
                "definition": j.get("definition"),
            }

            k = str(j.get("display", j.get("code")))
            k = re.sub(r"(?<!^)(?<![A-Z])(?=[A-Z])", "_", k).lower()
            k = re.sub(r"[^a-z0-9_]", "_", k)
            k = re.sub(r"_{2,}", "_", k)
            k = k if k[0].isalpha() else f"x{k}"
            if keyword.iskeyword(k):
                k = f"x_{k}"

            vd = {a: b for a, b in d.items() if b}

            ev.append((k, j.get("definition", j.get("display", j.get("code"))), vd))
        return ev


class ValueSet(ResourceFrame):
    class Meta(ResourceMeta):
        resource_type = ResourceType.VALUE_SET

    def concepts(self):
        ev: List[Tuple[str, str, str]] = []

        for i in self.Meta.definition["compose"]["include"]:
            if i.get("concept"):
                for j in i.get("concept", ()):
                    d = {
                        "system": i["system"],
                        "code": j["code"],
                        "display": j.get("display"),
                    }

                    k = str(j.get("display", j.get("code")))
                    k = re.sub(r"(?<!^)(?=[A-Z])", "_", k).lower()
                    k = re.sub(r"[^a-z0-9_]", "_", k)
                    k = re.sub(r"_{2,}", "_", k)
                    k = k if k[0].isalpha() else f"x{k}"

                    vd = dict(url=self.Meta.url)
                    if len(self.Meta.definition["compose"]["include"]) > 1:
                        vd["valueCoding"] = {a: b for a, b in d.items() if b}
                    elif d.get("display"):
                        vd["valueString"] = d.get("display")
                    else:
                        vd["valueCode"] = d.get("code")

                    ev.append((k, j.get("display", j.get("code")), vd))
            else:
                mod = f"oops_fhir.terminologies.{registry[i['system']]}"
                mod = import_module(mod)
                self.imports.add(mod.__name__)
                for concept in mod.__all__:
                    ev.append(
                        (
                            concept,
                            getattr(mod, concept)["definition"],
                            f"""{{
                            'url': _url_,
                            'valueCode': {mod.__name__.split('.')[-1]}.{concept}['code']
                        }}""",
                        )
                    )
        return ev


if __name__ == "__main__":
    # R4
    d = Path("r4")
    j = json.loads(Path(d, 'valuesets.json').read_text())
    for e in j['entry']:
        if e['resource']['resourceType'] == 'CodeSystem':
            print(e['resource']['id'])
            CodeSystem(e['resource'])
            break

    # ValueSet(f"{prefix}/r4/value_set/administrative_gender.json")
    # reg_p.write_text(
    #     json.dumps({k: registry[k] for k in sorted(registry.keys())}, indent=2)
    # )
