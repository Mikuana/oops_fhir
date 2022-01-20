from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AllergyIntoleranceSeverity"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AllergyIntoleranceSeverity:
    """
    AllergyIntoleranceSeverity

    Clinical assessment of the severity of a reaction event as a whole,
potentially considering multiple different manifestations.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/reaction-event-severity
    """

    mild = CodeSystemConcept(
        {
            "code": "mild",
            "definition": "Causes mild physiological effects.",
            "display": "Mild",
        }
    )
    """
    Mild

    Causes mild physiological effects.
    """

    moderate = CodeSystemConcept(
        {
            "code": "moderate",
            "definition": "Causes moderate physiological effects.",
            "display": "Moderate",
        }
    )
    """
    Moderate

    Causes moderate physiological effects.
    """

    severe = CodeSystemConcept(
        {
            "code": "severe",
            "definition": "Causes severe physiological effects.",
            "display": "Severe",
        }
    )
    """
    Severe

    Causes severe physiological effects.
    """

    class Meta:
        resource = _resource
