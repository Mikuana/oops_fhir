import json
import types
from importlib import import_module
from pathlib import Path

from fhir.resources.codesystem import CodeSystemConcept as _CodeSystemConcept

_registry = json.loads(
    Path(Path(__file__).parent, 'registry.json').read_text()
)


def lookup(url: str) -> types.ModuleType:
    """
    Perform module lookup of resource using URL

    :param url: uniform resource locator that can be used to directly access the
        specified resource.
    :return: a python module in this package which represents the specified
        resource.
    """
    return import_module(_registry[url])


class CodeSystem:
    pass


class CodeSystemConcept:
    def __init__(self, definition: dict):
        self._resource = _CodeSystemConcept.parse_obj(definition)
        self.full = definition

    def __str__(self):
        return self._resource.json()


class ValueSet:
    pass
