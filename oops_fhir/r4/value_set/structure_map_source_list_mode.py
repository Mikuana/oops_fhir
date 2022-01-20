from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.structure_map_source_list_mode import (
    StructureMapSourceListMode as StructureMapSourceListMode_,
)


__all__ = ["StructureMapSourceListMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class StructureMapSourceListMode(StructureMapSourceListMode_):
    """
    StructureMapSourceListMode

    If field is a list, how to manage the source.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/map-source-list-mode
    """

    class Meta:
        resource = _resource
