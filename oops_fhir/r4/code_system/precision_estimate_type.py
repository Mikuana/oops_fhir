from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["PrecisionEstimateType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class PrecisionEstimateType:
    """
    PrecisionEstimateType

    Method of reporting variability of estimates, such as confidence
intervals, interquartile range or standard deviation.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/precision-estimate-type
    """

    ci = CodeSystemConcept(
        {
            "code": "CI",
            "definition": "confidence interval.",
            "display": "confidence interval",
        }
    )
    """
    confidence interval

    confidence interval.
    """

    iqr = CodeSystemConcept(
        {
            "code": "IQR",
            "definition": "interquartile range.",
            "display": "interquartile range",
        }
    )
    """
    interquartile range

    interquartile range.
    """

    sd = CodeSystemConcept(
        {
            "code": "SD",
            "definition": "standard deviation.",
            "display": "standard deviation",
        }
    )
    """
    standard deviation

    standard deviation.
    """

    se = CodeSystemConcept(
        {"code": "SE", "definition": "standard error.", "display": "standard error"}
    )
    """
    standard error

    standard error.
    """

    class Meta:
        resource = _resource
