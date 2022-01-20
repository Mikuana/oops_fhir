from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3RoleLinkStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3RoleLinkStatus:
    """
    v3 Code System RoleLinkStatus

      Description:  Codes representing possible states of a RoleLink, as
defined by the RoleLink class state machine.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-RoleLinkStatus
    """

    normal = CodeSystemConcept(
        {
            "code": "NORMAL",
            "concept": [
                {
                    "code": "ACTIVE",
                    "definition": "Description: The state indicates the RoleLink is in progress.",
                    "display": "active",
                },
                {
                    "code": "CANCELLED",
                    "definition": "Description: The terminal state resulting from abandoning the RoleLink prior to or after activation.",
                    "display": "cancelled",
                },
                {
                    "code": "COMPLETED",
                    "definition": "Description: The terminal state representing the successful completion of the RoleLink.",
                    "display": "completed",
                },
                {
                    "code": "PENDING",
                    "definition": "Description: The state indicates the RoleLink has not yet become active.",
                    "display": "pending",
                },
            ],
            "definition": "Description: The 'typical' state. Excludes \"nullified\" which represents the termination state of a RoleLink instance that was created in error.",
            "display": "normal",
        }
    )
    """
    normal

    Description: The 'typical' state. Excludes "nullified" which represents the termination state of a RoleLink instance that was created in error.
    """

    nullified = CodeSystemConcept(
        {
            "code": "NULLIFIED",
            "definition": "Description: The state representing the termination of a RoleLink instance that was created in error.",
            "display": "nullified",
        }
    )
    """
    nullified

    Description: The state representing the termination of a RoleLink instance that was created in error.
    """

    class Meta:
        resource = _resource
