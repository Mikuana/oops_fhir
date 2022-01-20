from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ListStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ListStatus:
    """
    ListStatus

    The current state of the list.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/list-status
    """

    current = CodeSystemConcept(
        {
            "code": "current",
            "definition": "The list is considered to be an active part of the patient's record.",
            "display": "Current",
        }
    )
    """
    Current

    The list is considered to be an active part of the patient's record.
    """

    retired = CodeSystemConcept(
        {
            "code": "retired",
            "definition": 'The list is "old" and should no longer be considered accurate or relevant.',
            "display": "Retired",
        }
    )
    """
    Retired

    The list is "old" and should no longer be considered accurate or relevant.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The list was never accurate.  It is retained for medico-legal purposes only.",
            "display": "Entered In Error",
        }
    )
    """
    Entered In Error

    The list was never accurate.  It is retained for medico-legal purposes only.
    """

    class Meta:
        resource = _resource
