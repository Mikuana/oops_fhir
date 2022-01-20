from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.assertion_operator_type import (
    AssertionOperatorType as AssertionOperatorType_,
)


__all__ = ["AssertionOperatorType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AssertionOperatorType(AssertionOperatorType_):
    """
    AssertionOperatorType

    The type of operator to use for assertion.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/assert-operator-codes
    """

    class Meta:
        resource = _resource
