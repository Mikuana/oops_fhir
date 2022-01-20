from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.structure_map_group_type_mode import (
    StructureMapGroupTypeMode as StructureMapGroupTypeMode_,
)


__all__ = ["StructureMapGroupTypeMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class StructureMapGroupTypeMode(StructureMapGroupTypeMode_):
    """
    StructureMapGroupTypeMode

    If this is the default rule set to apply for the source type, or this
combination of types.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/map-group-type-mode
    """

    class Meta:
        resource = _resource
