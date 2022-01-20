from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.structure_map_target_list_mode import (
    StructureMapTargetListMode as StructureMapTargetListMode_,
)


__all__ = ["StructureMapTargetListMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class StructureMapTargetListMode(StructureMapTargetListMode_):
    """
    StructureMapTargetListMode

    If field is a list, how to manage the production.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/map-target-list-mode
    """

    class Meta:
        resource = _resource
