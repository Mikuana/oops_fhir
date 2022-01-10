import json
import subprocess
import sys
import textwrap
import warnings
from pathlib import Path
from typing import Union

import jinja2
from fhir.resources.bundle import Bundle

from structures.utils import snake_case, all_imps, namespace_imps, stage_values, register_urls, json_to_py

reg_p = Path("/home/chris/PycharmProjects/oops_fhir/oops_fhir/registry.json")
bp = Path("/home/chris/PycharmProjects/oops_fhir/structures/")
p2 = Path("/home/chris/PycharmProjects/oops_fhir/oops_fhir")

# TODO: re-enable us core
# sources = [("r4",), ("us", "core")]
sources = [("r4",)]

registry = json.loads(reg_p.read_text())
# registry = register_urls(sources)


loader = jinja2.FileSystemLoader('/home/chris/PycharmProjects/oops_fhir/structures/templates')
jinj_env = jinja2.Environment(
    loader=loader,
    extensions=['jinja2.ext.do']
)
jinj_env.filters['snake_case'] = snake_case
jinj_env.filters['wrap'] = lambda x: '\n'.join(textwrap.wrap(x, 72))
jinj_env.filters['all_imps'] = all_imps
jinj_env.filters['enumerate'] = enumerate
jinj_env.filters['namespace_imps'] = namespace_imps
jinj_env.filters['oops_ref'] = lambda x: registry.get(x)
jinj_env.filters['get_values'] = lambda x: stage_values(x, registry)
jinj_env.filters['json_to_py'] = json_to_py

build_order = ['CodeSystem', 'ValueSet']

for o in build_order:
    for source in sources:
        sp = Path(p2, *source)
        sp.mkdir(exist_ok=True, parents=True)
        Path(sp, "__init__.py").touch()
        bundle: Union[Bundle, None] = None
        resources = []
        for bj in Path(bp, *source).glob("*.json"):
            # if bj.name != 'valuesets.json':
            #     continue
            try:
                print(bj)
                bundle = Bundle.parse_file(bj)
            except Exception as e:
                j = json.loads(bj.read_text())
                resource_type = j.get("resourceType")
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

            # TODO: loop through all CodeSystems before ValueSets

            for resource in resources:
                if resource.resource_type != o:
                    continue
                elif resource.experimental is True:
                    continue
                elif resource.name == 'MessageEvent':  # TODO: wat?
                    continue  # this is a weird resource; I don't understand it
                elif resource.name == 'v3.policyHolderRole':
                    continue  # this CodeSystem claims to be complete, but is empty of concepts
                elif resource.name == 'SecurityRoleType':
                    continue  # this CodeSystem is missing from bundles, so ValueSet fails

                print(f'{resource.name} ({resource.resource_type})')

                resource.text = None
                rtp = Path(sp, snake_case(resource.resource_type))
                rtp.mkdir(exist_ok=True)
                Path(rtp, "__init__.py").touch()

                rp = Path(rtp, snake_case(resource.name))
                rp.with_suffix(".json").write_text(
                    json.dumps(json.loads(resource.json()), indent=2)
                )

                try:
                    template = jinj_env.get_template(
                        f'{snake_case(resource.resource_type)}.jinja2'
                    )
                    txt = template.render(resource=resource)

                    rp.with_suffix(".py").write_text(txt)
                    subprocess.check_call(
                        [sys.executable, "-m", "black", "-q", rp.with_suffix('.py')]
                    )
                except jinja2.TemplateNotFound as e:
                    warnings.warn(str(e))
