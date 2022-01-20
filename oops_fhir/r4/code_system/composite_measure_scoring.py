from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CompositeMeasureScoring"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CompositeMeasureScoring:
    """
    CompositeMeasureScoring

    The composite scoring method of the measure.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/composite-measure-scoring
    """

    opportunity = CodeSystemConcept(
        {
            "code": "opportunity",
            "definition": "Opportunity scoring combines the scores from component measures by combining the numerators and denominators for each component.",
            "display": "Opportunity",
        }
    )
    """
    Opportunity

    Opportunity scoring combines the scores from component measures by combining the numerators and denominators for each component.
    """

    all_or_nothing = CodeSystemConcept(
        {
            "code": "all-or-nothing",
            "definition": "All-or-nothing scoring includes an individual in the numerator of the composite measure if they are in the numerators of all of the component measures in which they are in the denominator.",
            "display": "All-or-nothing",
        }
    )
    """
    All-or-nothing

    All-or-nothing scoring includes an individual in the numerator of the composite measure if they are in the numerators of all of the component measures in which they are in the denominator.
    """

    linear = CodeSystemConcept(
        {
            "code": "linear",
            "definition": "Linear scoring gives an individual a score based on the number of numerators in which they appear.",
            "display": "Linear",
        }
    )
    """
    Linear

    Linear scoring gives an individual a score based on the number of numerators in which they appear.
    """

    weighted = CodeSystemConcept(
        {
            "code": "weighted",
            "definition": "Weighted scoring gives an individual a score based on a weighted factor for each component numerator in which they appear.",
            "display": "Weighted",
        }
    )
    """
    Weighted

    Weighted scoring gives an individual a score based on a weighted factor for each component numerator in which they appear.
    """

    class Meta:
        resource = _resource
