from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.conditional_delete_status import (
    ConditionalDeleteStatus as ConditionalDeleteStatus_,
)


__all__ = ["ConditionalDeleteStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConditionalDeleteStatus(ConditionalDeleteStatus_):
    """
    ConditionalDeleteStatus

    A code that indicates how the server supports conditional delete.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/conditional-delete-status
    """

    class Meta:
        resource = _resource
