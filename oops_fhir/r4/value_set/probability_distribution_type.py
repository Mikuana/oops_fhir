from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ProbabilityDistributionType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ProbabilityDistributionType(ValueSet):
    """
    ProbabilityDistributionType

    Codes specifying the type of probability distribution.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/probability-distribution-type
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
