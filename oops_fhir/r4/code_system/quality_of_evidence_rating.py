from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["QualityOfEvidenceRating"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class QualityOfEvidenceRating:
    """
    QualityOfEvidenceRating

    A rating system that describes the quality of evidence such as the
GRADE, DynaMed, or Oxford CEBM systems.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/evidence-quality
    """

    high = CodeSystemConcept(
        {
            "code": "high",
            "definition": "High quality evidence.",
            "display": "High quality",
        }
    )
    """
    High quality

    High quality evidence.
    """

    moderate = CodeSystemConcept(
        {
            "code": "moderate",
            "definition": "Moderate quality evidence.",
            "display": "Moderate quality",
        }
    )
    """
    Moderate quality

    Moderate quality evidence.
    """

    low = CodeSystemConcept(
        {"code": "low", "definition": "Low quality evidence.", "display": "Low quality"}
    )
    """
    Low quality

    Low quality evidence.
    """

    very_low = CodeSystemConcept(
        {
            "code": "very-low",
            "definition": "Very low quality evidence.",
            "display": "Very low quality",
        }
    )
    """
    Very low quality

    Very low quality evidence.
    """

    class Meta:
        resource = _resource
