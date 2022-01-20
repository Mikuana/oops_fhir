from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["RiskEstimateType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class RiskEstimateType:
    """
    RiskEstimateType

    Whether the risk estimate is dichotomous, continuous or qualitative and
the specific type of risk estimate (eg proportion or median).

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/risk-estimate-type
    """

    proportion = CodeSystemConcept(
        {
            "code": "proportion",
            "definition": "dichotomous measure (present or absent) reported as a ratio compared to the denominator of 1 (A percentage is a proportion with denominator of 100).",
            "display": "proportion",
        }
    )
    """
    proportion

    dichotomous measure (present or absent) reported as a ratio compared to the denominator of 1 (A percentage is a proportion with denominator of 100).
    """

    derived_proportion = CodeSystemConcept(
        {
            "code": "derivedProportion",
            "definition": "A special use case where the proportion is derived from a formula rather than derived from summary evidence.",
            "display": "derivedProportion",
        }
    )
    """
    derivedProportion

    A special use case where the proportion is derived from a formula rather than derived from summary evidence.
    """

    mean = CodeSystemConcept(
        {
            "code": "mean",
            "definition": "continuous numerical measure reported as an average.",
            "display": "mean",
        }
    )
    """
    mean

    continuous numerical measure reported as an average.
    """

    median = CodeSystemConcept(
        {
            "code": "median",
            "definition": "continuous numerical measure reported as the middle of the range.",
            "display": "median",
        }
    )
    """
    median

    continuous numerical measure reported as the middle of the range.
    """

    count = CodeSystemConcept(
        {
            "code": "count",
            "definition": "descriptive measure reported as total number of items.",
            "display": "count",
        }
    )
    """
    count

    descriptive measure reported as total number of items.
    """

    descriptive = CodeSystemConcept(
        {
            "code": "descriptive",
            "definition": "descriptive measure reported as narrative.",
            "display": "descriptive",
        }
    )
    """
    descriptive

    descriptive measure reported as narrative.
    """

    class Meta:
        resource = _resource
