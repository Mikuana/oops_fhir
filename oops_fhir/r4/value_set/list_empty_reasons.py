from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.list_empty_reasons import (
    ListEmptyReasons as ListEmptyReasons_,
)


__all__ = ["ListEmptyReasons"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ListEmptyReasons(ListEmptyReasons_):
    """
    List Empty Reasons

    General reasons for a list to be empty. Reasons are either related to a
summary list (i.e. problem or medication list) or to a workflow related
list (i.e. consultation list).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/list-empty-reason
    """

    class Meta:
        resource = _resource
