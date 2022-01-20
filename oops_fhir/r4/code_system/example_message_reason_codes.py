from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExampleMessageReasonCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExampleMessageReasonCodes:
    """
    Example Message Reason Codes

    Example Message Reasons. These are the set of codes that might be used
an updating an encounter using admin-update.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/message-reasons-encounter
    """

    admit = CodeSystemConcept(
        {
            "code": "admit",
            "definition": "The patient has been admitted.",
            "display": "Admit",
        }
    )
    """
    Admit

    The patient has been admitted.
    """

    discharge = CodeSystemConcept(
        {
            "code": "discharge",
            "definition": "The patient has been discharged.",
            "display": "Discharge",
        }
    )
    """
    Discharge

    The patient has been discharged.
    """

    absent = CodeSystemConcept(
        {
            "code": "absent",
            "definition": "The patient has temporarily left the institution.",
            "display": "Absent",
        }
    )
    """
    Absent

    The patient has temporarily left the institution.
    """

    return_ = CodeSystemConcept(
        {
            "code": "return",
            "definition": "The patient has returned from a temporary absence.",
            "display": "Returned",
        }
    )
    """
    Returned

    The patient has returned from a temporary absence.
    """

    moved = CodeSystemConcept(
        {
            "code": "moved",
            "definition": "The patient has been moved to a new location.",
            "display": "Moved",
        }
    )
    """
    Moved

    The patient has been moved to a new location.
    """

    edit = CodeSystemConcept(
        {
            "code": "edit",
            "definition": "Encounter details have been updated (e.g. to correct a coding error).",
            "display": "Edit",
        }
    )
    """
    Edit

    Encounter details have been updated (e.g. to correct a coding error).
    """

    class Meta:
        resource = _resource
