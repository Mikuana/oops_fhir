from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["FamilyHistoryStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class FamilyHistoryStatus:
    """
    FamilyHistoryStatus

    A code that identifies the status of the family history record.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/history-status
    """

    partial = CodeSystemConcept(
        {
            "code": "partial",
            "definition": "Some health information is known and captured, but not complete - see notes for details.",
            "display": "Partial",
        }
    )
    """
    Partial

    Some health information is known and captured, but not complete - see notes for details.
    """

    completed = CodeSystemConcept(
        {
            "code": "completed",
            "definition": "All available related health information is captured as of the date (and possibly time) when the family member history was taken.",
            "display": "Completed",
        }
    )
    """
    Completed

    All available related health information is captured as of the date (and possibly time) when the family member history was taken.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "This instance should not have been part of this patient's medical record.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    This instance should not have been part of this patient's medical record.
    """

    health_unknown = CodeSystemConcept(
        {
            "code": "health-unknown",
            "definition": "Health information for this family member is unavailable/unknown.",
            "display": "Health Unknown",
        }
    )
    """
    Health Unknown

    Health information for this family member is unavailable/unknown.
    """

    class Meta:
        resource = _resource
