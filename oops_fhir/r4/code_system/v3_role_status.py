from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3RoleStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3RoleStatus:
    """
    v3 Code System RoleStatus

     Codes representing the defined possible states of an Role, as defined
by the Role class state machine.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-RoleStatus
    """

    normal = CodeSystemConcept(
        {
            "code": "normal",
            "concept": [
                {
                    "code": "active",
                    "definition": "The state representing the fact that the Entity is currently active in the Role.",
                    "display": "active",
                },
                {
                    "code": "cancelled",
                    "definition": "The terminal state resulting from cancellation of the role prior to activation.",
                    "display": "cancelled",
                },
                {
                    "code": "pending",
                    "definition": "The state representing that fact that the role has not yet become active.",
                    "display": "pending",
                },
                {
                    "code": "suspended",
                    "definition": 'The state that represents a suspension of the Entity playing the Role. This state is arrived at from the "active" state.',
                    "display": "suspended",
                },
                {
                    "code": "terminated",
                    "definition": "The state representing the successful termination of the Role.",
                    "display": "terminated",
                },
            ],
            "definition": "The 'typical' state. Excludes \"nullified\" which represents the termination state of a Role instance that was created in error.",
            "display": "normal",
        }
    )
    """
    normal

    The 'typical' state. Excludes "nullified" which represents the termination state of a Role instance that was created in error.
    """

    nullified = CodeSystemConcept(
        {
            "code": "nullified",
            "definition": "The state representing the termination of a Role instance that was created in error.",
            "display": "nullified",
        }
    )
    """
    nullified

    The state representing the termination of a Role instance that was created in error.
    """

    class Meta:
        resource = _resource
