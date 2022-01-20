from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MeasureImprovementNotation"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MeasureImprovementNotation:
    """
    MeasureImprovementNotation

    Observation values that indicate what change in a measurement value or
score is indicative of an improvement in the measured item or scored
issue.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/measure-improvement-notation
    """

    increase = CodeSystemConcept(
        {
            "code": "increase",
            "definition": "Improvement is indicated as an increase in the score or measurement (e.g. Higher score indicates better quality).",
            "display": "Increased score indicates improvement",
        }
    )
    """
    Increased score indicates improvement

    Improvement is indicated as an increase in the score or measurement (e.g. Higher score indicates better quality).
    """

    decrease = CodeSystemConcept(
        {
            "code": "decrease",
            "definition": "Improvement is indicated as a decrease in the score or measurement (e.g. Lower score indicates better quality).",
            "display": "Decreased score indicates improvement",
        }
    )
    """
    Decreased score indicates improvement

    Improvement is indicated as a decrease in the score or measurement (e.g. Lower score indicates better quality).
    """

    class Meta:
        resource = _resource
