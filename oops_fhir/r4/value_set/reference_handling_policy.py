from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.reference_handling_policy import (
    ReferenceHandlingPolicy as ReferenceHandlingPolicy_,
)


__all__ = ["ReferenceHandlingPolicy"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ReferenceHandlingPolicy(ReferenceHandlingPolicy_):
    """
    ReferenceHandlingPolicy

    A set of flags that defines how references are supported.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/reference-handling-policy
    """

    class Meta:
        resource = _resource
