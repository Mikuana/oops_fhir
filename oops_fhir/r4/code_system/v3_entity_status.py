from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3EntityStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityStatus:
    """
    v3 Code System EntityStatus

     Codes representing the defined possible states of an Entity, as defined
by the Entity class state machine.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-EntityStatus
    """

    normal = CodeSystemConcept(
        {
            "code": "normal",
            "concept": [
                {
                    "code": "active",
                    "definition": "The state representing the fact that the Entity record is currently active.",
                    "display": "active",
                },
                {
                    "code": "inactive",
                    "definition": "Definition: The state representing the fact that the entity is inactive.",
                    "display": "inactive",
                },
                {
                    "code": "terminated",
                    "definition": "The state representing the normal termination of an Entity record.",
                    "display": "terminated",
                    "property": [{"code": "status", "valueCode": "retired"}],
                },
            ],
            "definition": "The 'typical' state. Excludes \"nullified\" which represents the termination state of an Entity record instance that was created in error.",
            "display": "normal",
        }
    )
    """
    normal

    The 'typical' state. Excludes "nullified" which represents the termination state of an Entity record instance that was created in error.
    """

    nullified = CodeSystemConcept(
        {
            "code": "nullified",
            "definition": "The state representing the termination of an Entity record instance that was created in error.",
            "display": "nullified",
        }
    )
    """
    nullified

    The state representing the termination of an Entity record instance that was created in error.
    """

    class Meta:
        resource = _resource
