from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.conformance_expectation import (
    ConformanceExpectation as ConformanceExpectation_,
)


__all__ = ["ConformanceExpectation"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConformanceExpectation(ConformanceExpectation_):
    """
    ConformanceExpectation

    Indicates the degree of adherence to a specified behavior or capability
expected for a system to be deemed conformant with a specification.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/conformance-expectation
    """

    class Meta:
        resource = _resource
