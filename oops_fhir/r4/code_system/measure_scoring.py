from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MeasureScoring"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MeasureScoring:
    """
    MeasureScoring

    The scoring type of the measure.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/measure-scoring
    """

    proportion = CodeSystemConcept(
        {
            "code": "proportion",
            "definition": "The measure score is defined using a proportion.",
            "display": "Proportion",
        }
    )
    """
    Proportion

    The measure score is defined using a proportion.
    """

    ratio = CodeSystemConcept(
        {
            "code": "ratio",
            "definition": "The measure score is defined using a ratio.",
            "display": "Ratio",
        }
    )
    """
    Ratio

    The measure score is defined using a ratio.
    """

    continuous_variable = CodeSystemConcept(
        {
            "code": "continuous-variable",
            "definition": "The score is defined by a calculation of some quantity.",
            "display": "Continuous Variable",
        }
    )
    """
    Continuous Variable

    The score is defined by a calculation of some quantity.
    """

    cohort = CodeSystemConcept(
        {
            "code": "cohort",
            "definition": "The measure is a cohort definition.",
            "display": "Cohort",
        }
    )
    """
    Cohort

    The measure is a cohort definition.
    """

    class Meta:
        resource = _resource
