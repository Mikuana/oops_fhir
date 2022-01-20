from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CareTeamStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CareTeamStatus:
    """
    CareTeamStatus

    Indicates the status of the care team.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/care-team-status
    """

    proposed = CodeSystemConcept(
        {
            "code": "proposed",
            "definition": "The care team has been drafted and proposed, but not yet participating in the coordination and delivery of patient care.",
            "display": "Proposed",
        }
    )
    """
    Proposed

    The care team has been drafted and proposed, but not yet participating in the coordination and delivery of patient care.
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "The care team is currently participating in the coordination and delivery of care.",
            "display": "Active",
        }
    )
    """
    Active

    The care team is currently participating in the coordination and delivery of care.
    """

    suspended = CodeSystemConcept(
        {
            "code": "suspended",
            "definition": "The care team is temporarily on hold or suspended and not participating in the coordination and delivery of care.",
            "display": "Suspended",
        }
    )
    """
    Suspended

    The care team is temporarily on hold or suspended and not participating in the coordination and delivery of care.
    """

    inactive = CodeSystemConcept(
        {
            "code": "inactive",
            "definition": "The care team was, but is no longer, participating in the coordination and delivery of care.",
            "display": "Inactive",
        }
    )
    """
    Inactive

    The care team was, but is no longer, participating in the coordination and delivery of care.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The care team should have never existed.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The care team should have never existed.
    """

    class Meta:
        resource = _resource
