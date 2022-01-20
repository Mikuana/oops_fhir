from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.sort_direction import SortDirection as SortDirection_


__all__ = ["SortDirection"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SortDirection(SortDirection_):
    """
    SortDirection

    The possible sort directions, ascending or descending.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/sort-direction
    """

    class Meta:
        resource = _resource
