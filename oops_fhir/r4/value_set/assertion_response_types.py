from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.assertion_response_types import (
    AssertionResponseTypes as AssertionResponseTypes_,
)


__all__ = ["AssertionResponseTypes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AssertionResponseTypes(AssertionResponseTypes_):
    """
    AssertionResponseTypes

    The type of response code to use for assertion.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/assert-response-code-types
    """

    class Meta:
        resource = _resource
