from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MedicationKnowledgeStatusCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MedicationKnowledgeStatusCodes:
    """
    Medication knowledge  status  codes

    MedicationKnowledge Status Codes

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/medicationknowledge-status
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "The medication is available for use.",
            "display": "Active",
        }
    )
    """
    Active

    The medication is available for use.
    """

    inactive = CodeSystemConcept(
        {
            "code": "inactive",
            "definition": "The medication is not available for use.",
            "display": "Inactive",
        }
    )
    """
    Inactive

    The medication is not available for use.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The medication was entered in error.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The medication was entered in error.
    """

    class Meta:
        resource = _resource
