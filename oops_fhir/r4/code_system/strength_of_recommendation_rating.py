from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["StrengthOfRecommendationRating"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class StrengthOfRecommendationRating:
    """
    StrengthOfRecommendationRating

    A rating system that describes the strength of the recommendation, such
as the GRADE, DynaMed, or HGPS systems.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/recommendation-strength
    """

    strong = CodeSystemConcept(
        {"code": "strong", "definition": "Strong recommendation.", "display": "Strong"}
    )
    """
    Strong

    Strong recommendation.
    """

    weak = CodeSystemConcept(
        {"code": "weak", "definition": "Weak recommendation.", "display": "Weak"}
    )
    """
    Weak

    Weak recommendation.
    """

    class Meta:
        resource = _resource
