import json
from fhir.resources.codesystem import CodeSystemConcept as c1


class CodeSystemConceptFrame:
    resource: c1

    def __repr__(self):
        return self.resource.json()
