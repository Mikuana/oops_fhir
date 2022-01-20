from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["RiskProbability"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class RiskProbability:
    """
    Risk Probability

    Codes representing the likelihood of a particular outcome in a risk
assessment.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/risk-probability
    """

    negligible = CodeSystemConcept(
        {
            "code": "negligible",
            "definition": "The specified outcome is exceptionally unlikely.",
            "display": "Negligible likelihood",
        }
    )
    """
    Negligible likelihood

    The specified outcome is exceptionally unlikely.
    """

    low = CodeSystemConcept(
        {
            "code": "low",
            "definition": "The specified outcome is possible but unlikely.",
            "display": "Low likelihood",
        }
    )
    """
    Low likelihood

    The specified outcome is possible but unlikely.
    """

    moderate = CodeSystemConcept(
        {
            "code": "moderate",
            "definition": "The specified outcome has a reasonable likelihood of occurrence.",
            "display": "Moderate likelihood",
        }
    )
    """
    Moderate likelihood

    The specified outcome has a reasonable likelihood of occurrence.
    """

    high = CodeSystemConcept(
        {
            "code": "high",
            "definition": "The specified outcome is more likely to occur than not.",
            "display": "High likelihood",
        }
    )
    """
    High likelihood

    The specified outcome is more likely to occur than not.
    """

    certain = CodeSystemConcept(
        {
            "code": "certain",
            "definition": "The specified outcome is effectively guaranteed.",
            "display": "Certain",
        }
    )
    """
    Certain

    The specified outcome is effectively guaranteed.
    """

    class Meta:
        resource = _resource
