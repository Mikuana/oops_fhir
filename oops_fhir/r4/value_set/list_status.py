from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.list_status import ListStatus as ListStatus_


__all__ = ["ListStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ListStatus(ListStatus_):
    """
    ListStatus

    The current state of the list.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/list-status
    """

    class Meta:
        resource = _resource
