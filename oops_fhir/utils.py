from fhir.resources.codesystem import CodeSystemConcept as _CodeSystemConcept


class CodeSystemConcept:
    def __init__(self, definition: dict):
        self._resource = _CodeSystemConcept.parse_obj(definition)
        self.full = definition

    def __str__(self):
        return self._resource.json()


class ValueSetConcept:
    pass
