from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.assertion_direction_type import (
    AssertionDirectionType as AssertionDirectionType_,
)


__all__ = ["AssertionDirectionType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AssertionDirectionType(AssertionDirectionType_):
    """
    AssertionDirectionType

    The type of direction to use for assertion.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/assert-direction-codes
    """

    class Meta:
        resource = _resource
