from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_probability_distribution_type import (
    v3ProbabilityDistributionType as v3ProbabilityDistributionType_,
)


__all__ = ["v3ProbabilityDistributionType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ProbabilityDistributionType(v3ProbabilityDistributionType_):
    """
    v3 Code System ProbabilityDistributionType

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ProbabilityDistributionType
    """

    class Meta:
        resource = _resource
