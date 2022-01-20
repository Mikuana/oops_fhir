from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ManagedParticipationStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ManagedParticipationStatus:
    """
    v3 Code System ManagedParticipationStatus

     Codes representing the defined possible states of a Managed
Participation, as defined by the Managed Participation class state
machine.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ManagedParticipationStatus
    """

    normal = CodeSystemConcept(
        {
            "code": "normal",
            "concept": [
                {
                    "code": "active",
                    "definition": "The state representing the fact that the Participation is in progress.",
                    "display": "active",
                },
                {
                    "code": "cancelled",
                    "definition": "The terminal state resulting from cancellation of the Participation prior to activation.",
                    "display": "cancelled",
                },
                {
                    "code": "completed",
                    "definition": "The terminal state representing the successful completion of the Participation.",
                    "display": "completed",
                },
                {
                    "code": "pending",
                    "definition": "The state representing that fact that the Participation has not yet become active.",
                    "display": "pending",
                },
            ],
            "definition": "The 'typical' state. Excludes \"nullified\" which represents the termination state of a participation instance that was created in error.",
            "display": "normal",
        }
    )
    """
    normal

    The 'typical' state. Excludes "nullified" which represents the termination state of a participation instance that was created in error.
    """

    nullified = CodeSystemConcept(
        {
            "code": "nullified",
            "definition": "The state representing the termination of a Participation instance that was created in error.",
            "display": "nullified",
        }
    )
    """
    nullified

    The state representing the termination of a Participation instance that was created in error.
    """

    class Meta:
        resource = _resource
