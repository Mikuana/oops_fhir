from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AllergyIntoleranceCriticality"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AllergyIntoleranceCriticality:
    """
    AllergyIntoleranceCriticality

    Estimate of the potential clinical harm, or seriousness, of a reaction
to an identified substance.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/allergy-intolerance-criticality
    """

    low = CodeSystemConcept(
        {
            "code": "low",
            "definition": "Worst case result of a future exposure is not assessed to be life-threatening or having high potential for organ system failure.",
            "display": "Low Risk",
        }
    )
    """
    Low Risk

    Worst case result of a future exposure is not assessed to be life-threatening or having high potential for organ system failure.
    """

    high = CodeSystemConcept(
        {
            "code": "high",
            "definition": "Worst case result of a future exposure is assessed to be life-threatening or having high potential for organ system failure.",
            "display": "High Risk",
        }
    )
    """
    High Risk

    Worst case result of a future exposure is assessed to be life-threatening or having high potential for organ system failure.
    """

    unable_to_assess = CodeSystemConcept(
        {
            "code": "unable-to-assess",
            "definition": "Unable to assess the worst case result of a future exposure.",
            "display": "Unable to Assess Risk",
        }
    )
    """
    Unable to Assess Risk

    Unable to assess the worst case result of a future exposure.
    """

    class Meta:
        resource = _resource
