from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.precision_estimate_type import (
    PrecisionEstimateType as PrecisionEstimateType_,
)


__all__ = ["PrecisionEstimateType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class PrecisionEstimateType(PrecisionEstimateType_):
    """
    PrecisionEstimateType

    Method of reporting variability of estimates, such as confidence
intervals, interquartile range or standard deviation.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/precision-estimate-type
    """

    class Meta:
        resource = _resource
