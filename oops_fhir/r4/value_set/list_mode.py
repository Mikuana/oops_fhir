from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.list_mode import ListMode as ListMode_


__all__ = ["ListMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ListMode(ListMode_):
    """
    ListMode

    The processing mode that applies to this list.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/list-mode
    """

    class Meta:
        resource = _resource
