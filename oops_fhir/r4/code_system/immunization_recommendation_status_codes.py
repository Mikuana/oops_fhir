from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ImmunizationRecommendationStatusCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationRecommendationStatusCodes:
    """
    Immunization Recommendation Status Codes

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the status of the patient towards
perceived immunity against a vaccine preventable disease. This value set
is provided as a suggestive example.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/immunization-recommendation-status
    """

    due = CodeSystemConcept(
        {
            "code": "due",
            "definition": "The patient is due for their next vaccination.",
            "display": "Due",
        }
    )
    """
    Due

    The patient is due for their next vaccination.
    """

    overdue = CodeSystemConcept(
        {
            "code": "overdue",
            "definition": "The patient is considered overdue for their next vaccination.",
            "display": "Overdue",
        }
    )
    """
    Overdue

    The patient is considered overdue for their next vaccination.
    """

    immune = CodeSystemConcept(
        {
            "code": "immune",
            "definition": "The patient is immune to the target disease and further immunization against the disease is not likely to provide benefit.",
            "display": "Immune",
        }
    )
    """
    Immune

    The patient is immune to the target disease and further immunization against the disease is not likely to provide benefit.
    """

    contraindicated = CodeSystemConcept(
        {
            "code": "contraindicated",
            "definition": "The patient is contraindicated for futher doses.",
            "display": "Contraindicated",
        }
    )
    """
    Contraindicated

    The patient is contraindicated for futher doses.
    """

    complete = CodeSystemConcept(
        {
            "code": "complete",
            "definition": "The patient is fully protected and no further doses are recommended.",
            "display": "Complete",
        }
    )
    """
    Complete

    The patient is fully protected and no further doses are recommended.
    """

    class Meta:
        resource = _resource
