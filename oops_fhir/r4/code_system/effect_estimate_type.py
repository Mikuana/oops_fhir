from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["EffectEstimateType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class EffectEstimateType:
    """
    EffectEstimateType

    Whether the effect estimate is an absolute effect estimate (absolute
difference) or a relative effect estimate (relative difference), and the
specific type of effect estimate (eg relative risk or median
difference).

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/effect-estimate-type
    """

    relative_rr = CodeSystemConcept(
        {
            "code": "relative-RR",
            "definition": "relative risk (a type of relative effect estimate).",
            "display": "relative risk",
        }
    )
    """
    relative risk

    relative risk (a type of relative effect estimate).
    """

    relative_or = CodeSystemConcept(
        {
            "code": "relative-OR",
            "definition": "odds ratio (a type of relative effect estimate).",
            "display": "odds ratio",
        }
    )
    """
    odds ratio

    odds ratio (a type of relative effect estimate).
    """

    relative_hr = CodeSystemConcept(
        {
            "code": "relative-HR",
            "definition": "hazard ratio (a type of relative effect estimate).",
            "display": "hazard ratio",
        }
    )
    """
    hazard ratio

    hazard ratio (a type of relative effect estimate).
    """

    absolute_ard = CodeSystemConcept(
        {
            "code": "absolute-ARD",
            "definition": "absolute risk difference (a type of absolute effect estimate).",
            "display": "absolute risk difference",
        }
    )
    """
    absolute risk difference

    absolute risk difference (a type of absolute effect estimate).
    """

    absolute_mean_diff = CodeSystemConcept(
        {
            "code": "absolute-MeanDiff",
            "definition": "mean difference (a type of absolute effect estimate).",
            "display": "mean difference",
        }
    )
    """
    mean difference

    mean difference (a type of absolute effect estimate).
    """

    absolute_smd = CodeSystemConcept(
        {
            "code": "absolute-SMD",
            "definition": "standardized mean difference (a type of absolute effect estimate).",
            "display": "standardized mean difference",
        }
    )
    """
    standardized mean difference

    standardized mean difference (a type of absolute effect estimate).
    """

    absolute_median_diff = CodeSystemConcept(
        {
            "code": "absolute-MedianDiff",
            "definition": "median difference (a type of absolute effect estimate).",
            "display": "median difference",
        }
    )
    """
    median difference

    median difference (a type of absolute effect estimate).
    """

    class Meta:
        resource = _resource
