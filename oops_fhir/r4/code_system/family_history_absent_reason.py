from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["FamilyHistoryAbsentReason"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class FamilyHistoryAbsentReason:
    """
    FamilyHistoryAbsentReason

    Codes describing the reason why a family member's history is not
available.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/history-absent-reason
    """

    subject_unknown = CodeSystemConcept(
        {
            "code": "subject-unknown",
            "definition": "Patient does not know the subject, e.g. the biological parent of an adopted patient.",
            "display": "Subject Unknown",
        }
    )
    """
    Subject Unknown

    Patient does not know the subject, e.g. the biological parent of an adopted patient.
    """

    withheld = CodeSystemConcept(
        {
            "code": "withheld",
            "definition": "The patient withheld or refused to share the information.",
            "display": "Information Withheld",
        }
    )
    """
    Information Withheld

    The patient withheld or refused to share the information.
    """

    unable_to_obtain = CodeSystemConcept(
        {
            "code": "unable-to-obtain",
            "definition": "Information cannot be obtained; e.g. unconscious patient.",
            "display": "Unable To Obtain",
        }
    )
    """
    Unable To Obtain

    Information cannot be obtained; e.g. unconscious patient.
    """

    deferred = CodeSystemConcept(
        {
            "code": "deferred",
            "definition": "Patient does not have the information now, but can provide the information at a later date.",
            "display": "Deferred",
        }
    )
    """
    Deferred

    Patient does not have the information now, but can provide the information at a later date.
    """

    class Meta:
        resource = _resource
