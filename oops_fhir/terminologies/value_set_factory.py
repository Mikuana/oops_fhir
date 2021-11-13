import json
import keyword
import re
import subprocess
import sys
import textwrap
from enum import Enum
from pathlib import Path
from typing import Tuple, List, Any

reg_p = Path(Path(__file__).parent, 'registry.json')
registry = json.loads(reg_p.read_text())


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
    class Meta(ResourceMeta):
        pass

    def __init__(self, json_file_name):
        pd = Path(Path(__file__).parent, "r4", self.Meta.resource_type.value)
        with Path(pd, json_file_name) as f:
            self.Meta.location = f.relative_to(Path(__file__).parent).with_suffix('').as_posix().replace('/', '.')
            self.Meta.raw_json = f.read_text()

        self.Meta.definition = json.loads(self.Meta.raw_json)
        self.__doc__ = self.Meta.definition["description"]
        self.Meta.url = self.Meta.definition["url"]

        self.Meta.target = Path(
            Path(pd, self.Meta.definition.get("id").replace("-", "_"))
        ).with_suffix(".py")

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
        return ev

    def pythonize(self):
        values = [
            f"{name} = {value}\n" + (f'""" {desc} """\n' if desc else "")
            for name, desc, value in self.concepts()
        ]
        all_values = [name for name, _, _ in self.concepts()]
        self.Meta.target.write_text(
            '"""'
            + "\n".join(textwrap.wrap(self.__doc__, 72))
            + '"""\n\n'
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
        registry[self.Meta.url] = self.Meta.location


class CodeSystem(ResourceFrame):
    class Meta(ResourceMeta):
        resource_type = ResourceType.CODE_SYSTEM

    def concepts(self):
        ev: List[Tuple[str, str, dict]] = []
        for j in self.Meta.definition.get("concept", ()):
            d = {
                "code": j['code'],
                "display": j["display"],
                "definition": j.get("definition"),
            }

            k = str(j.get("display", j.get("code")))
            k = re.sub(r"(?<!^)(?=[A-Z])", "_", k).lower()
            k = re.sub(r"[^a-z0-9_]", "_", k)
            k = re.sub(r"_{2,}", "_", k)
            k = k if k[0].isalpha() else f"x{k}"
            if keyword.iskeyword(k):
                k = f'x_{k}'

            vd = {a: b for a, b in d.items() if b}

            ev.append((k, j.get("definition", j.get("display", j.get("code"))), vd))
        return ev


class ValueSet(ResourceFrame):
    class Meta(ResourceMeta):
        resource_type = ResourceType.VALUE_SET


if __name__ == '__main__':
    for vs in Path(r'/home/chris/PycharmProjects/oops_fhir/oops_fhir/terminologies/r4/code_system').glob("*.json"):
        print(vs.name)
        CodeSystem(vs.name)
        # break

    reg_p.write_text(json.dumps(
        {k: registry[k] for k in sorted(registry.keys())}, indent=2
    ))
