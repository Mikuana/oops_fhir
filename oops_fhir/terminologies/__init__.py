from fhir.resources.codesystem import CodeSystemConcept as c1
from fhir.resources.valueset import ValueSet as c2


class CodeSystemConceptFrame:
    resource: c1

    def __repr__(self):
        return self.resource.json()


class ValueSetComposeFrame:
    resource: c2

    def __repr__(self):
        return self.resource.json()
