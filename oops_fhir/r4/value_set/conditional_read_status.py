from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.conditional_read_status import (
    ConditionalReadStatus as ConditionalReadStatus_,
)


__all__ = ["ConditionalReadStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConditionalReadStatus(ConditionalReadStatus_):
    """
    ConditionalReadStatus

    A code that indicates how the server supports conditional read.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/conditional-read-status
    """

    class Meta:
        resource = _resource
