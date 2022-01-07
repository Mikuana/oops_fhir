import json
import subprocess
import sys
import textwrap
from pathlib import Path
from typing import Union

from fhir.resources.bundle import Bundle

from structures.utils import snake_case
from structures.parser.code_system import concepts

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
            rtp = Path(sp, snake_case(resource.resource_type))
            rp = Path(rtp, snake_case(resource.name))
            registry[resource.url] = (
                rp.relative_to("/home/chris/PycharmProjects/oops_fhir/")
                    .as_posix()
                    .replace("/", ".")
            )

        for resource in resources:
            # TODO: remove this loop skip
            if resource.id != 'abstract-types':
                continue

            resource.text = None
            rtp = Path(sp, snake_case(resource.resource_type))
            rtp.mkdir(exist_ok=True)
            Path(rtp, "__init__.py").touch()

            rp = Path(rtp, snake_case(resource.name))
            rp.with_suffix(".json").write_text(
                json.dumps(json.loads(resource.json()), indent=2)
            )

            txt = (
                textwrap.dedent(
                    f'''
                """
                {resource.name}

                {resource.description}

                {resource.url}
                """

                from pathlib import Path

                from fhir.resources.{resource.resource_type.lower()} import {resource.resource_type}
                # TODO: import referenced resources

                resource = {resource.resource_type}.parse_file(Path(__file__).with_suffix('.json'))
                '''
                )
            )

            if resource.resource_type == 'CodeSystem':
                txt += '\n' + concepts(resource)

            rp.with_suffix(".py").write_text(txt)
            subprocess.check_call(
                [sys.executable, "-m", "black", "-q", rp.with_suffix('.py')]
            )

reg_p = Path("/home/chris/PycharmProjects/oops_fhir/oops_fhir/registry.json")
reg_p.write_text(
    json.dumps({k: registry[k] for k in sorted(registry.keys())}, indent=2)
)
