import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Tuple, List


class ValueSet:
    class Meta:
        raw_json: str
        """ Raw JSON string which defines the resource """

        definition: dict
        """ Dictionary object parsed from raw JSON string """

        target: Path
        """ Target python script for the resource """

        url: str
        """ Resolvable URL to resource type definition """

    def __init__(self, json_file_name):
        with Path(Path(__file__).parent, json_file_name) as f:
            self.Meta.raw_json = f.read_text()

        self.Meta.definition = json.loads(self.Meta.raw_json)
        self.__doc__ = self.Meta.definition["description"]
        self.Meta.url = self.Meta.definition["url"]

        self.Meta.target = Path(
            Path(
                Path(__file__).parent, self.Meta.definition.get("id").replace("-", "_")
            )
        ).with_suffix(".py")

        self.pythonize()

    def expanded_values(self):
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
            for name, desc, value in self.expanded_values()
        ]
        ats = {
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

        self.Meta.target.write_text(
            "\n".join(
                [
                    f"_{v}_ = "
                    + (
                        f'"""{self.Meta.definition.get(k)}"""'
                        if isinstance(self.Meta.definition.get(k), str)
                        else str(self.Meta.definition.get(k))
                    )
                    for k, v in ats.items()
                ]
            )
            + "\n\n"
            + "\n".join(values)
        )
        subprocess.check_call(
            [sys.executable, "-m", "black", "-q", self.Meta.target.as_posix()]
        )


for vs in Path(Path(__file__).parent).glob("*.json"):
    print(vs.name)
    ValueSet(vs.name)
