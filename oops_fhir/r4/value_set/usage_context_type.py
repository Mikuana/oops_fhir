from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.usage_context_type import (
    UsageContextType as UsageContextType_,
)


__all__ = ["UsageContextType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class UsageContextType(UsageContextType_):
    """
    UsageContextType

    A code that specifies a type of context being specified by a usage
context.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/usage-context-type
    """

    class Meta:
        resource = _resource
