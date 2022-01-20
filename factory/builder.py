import json
import logging
import subprocess
import sys
import textwrap
from pathlib import Path
from typing import Union

import jinja2
from fhir.resources.bundle import Bundle

from factory.utils import (
    snake_case, all_imps, namespace_imps, stage_values, json_to_py, camel_case
)

factory_path = Path(Path(__file__).parent)
package_path = Path(factory_path.parent, "oops_fhir")

logging.basicConfig(
    filename=Path(factory_path, 'build.log'),
    filemode='w', encoding='utf-8', level=logging.INFO
)

registry = json.loads(Path(package_path, "registry.json").read_text())

sources = [("r4",)]

loader = jinja2.FileSystemLoader(Path(Path(__file__).parent, 'templates'))
jinj_env = jinja2.Environment(loader=loader, extensions=['jinja2.ext.do'])
jinj_env.filters['snake_case'] = snake_case
jinj_env.filters['camel_case'] = camel_case
jinj_env.filters['wrap'] = lambda x: '\n'.join(textwrap.wrap(x, 72))
jinj_env.filters['all_imps'] = all_imps
jinj_env.filters['enumerate'] = enumerate
jinj_env.filters['namespace_imps'] = namespace_imps
jinj_env.filters['oops_ref'] = lambda x: registry.get(x)
jinj_env.filters['get_values'] = lambda x: stage_values(x, registry)
jinj_env.filters['json_to_py'] = json_to_py

build_order = [
    'CodeSystem',
    'ValueSet'
]
experimental_exception = [
    'http://hl7.org/fhir/ValueSet/languages'
]

ignore = [
    'MessageEvent',  # TODO: wat? this resource is really weird
    'v3.policyHolderRole',  # CodeSystem says itscomplete, but is empty of concepts.
    'SecurityRoleType',  # CodeSystem is missing from bundles, ValueSet fails
    'ParticipationRoleType',  # CodeSystem is missing from bundles, ValueSet fails
]

for o in build_order:
    logging.info(f'Building resource type {o}')
    for source in sources:
        logging.info(f'Loading source files for "{source}"')
        sp = Path(package_path, *source)
        sp.mkdir(exist_ok=True, parents=True)
        Path(sp, "__init__.py").touch()
        bundle: Union[Bundle, None] = None
        resources = []
        for bj in Path(factory_path, *source).glob("*.json"):
            logging.info(
                f'Parsing source file {bj.relative_to(Path(__file__).parent)}'
            )
            try:
                bundle = Bundle.parse_file(bj)
            except Exception as e:
                j = json.loads(bj.read_text())
                resource_type = j.get("resourceType")
                if resource_type == "ImplementationGuide" or bj.name == 'v2-tables.json':
                    logging.warning(f'Skipping file {bj.name}')
                    continue
                elif resource_type:
                    logging.info(f'Importing {bj.name} as {resource_type}')

                    from importlib import import_module

                    module = import_module(f"fhir.resources.{resource_type.lower()}")
                    resources.append(getattr(module, resource_type).parse_file(bj))
                else:
                    logging.error(f'Failed while parsing file {bj.name}')
                    continue

            if bundle:
                # noinspection PyUnresolvedReferences
                resources = [e.resource for e in bundle.entry]

            for resource in resources:
                if resource.resource_type != o:
                    continue
                elif resource.experimental is True and \
                    resource.url not in experimental_exception:
                    continue
                elif resource.name in ignore:
                    logging.info(f'Ignoring {resource.resource_type} resource {resource.name}')
                    continue

                resource.text = None  # remove text to reduce size
                rtp = Path(sp, snake_case(resource.resource_type))
                rtp.mkdir(exist_ok=True)
                Path(rtp, "__init__.py").touch()

                rp = Path(rtp, snake_case(resource.name))
                rp.with_suffix(".json").write_text(
                    json.dumps(json.loads(resource.json()), indent=2)
                )

                try:
                    logging.info(
                        f'Rendering {resource.resource_type} {resource.name} template'
                    )
                    template = jinj_env.get_template(
                        f'{snake_case(resource.resource_type)}.jinja2'
                    )
                    txt = template.render(resource=resource)

                    rp.with_suffix(".py").write_text(txt)
                    subprocess.check_call(
                        [sys.executable, "-m", "black", "-q", rp.with_suffix('.py')]
                    )
                except jinja2.TemplateNotFound as e:
                    logging.warning(f'No template defined for {resource.resource_type}')
                except Exception as e:
                    logging.exception(e)
                    raise e
