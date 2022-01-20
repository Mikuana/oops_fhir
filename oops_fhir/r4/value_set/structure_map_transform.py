from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.structure_map_transform import (
    StructureMapTransform as StructureMapTransform_,
)


__all__ = ["StructureMapTransform"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class StructureMapTransform(StructureMapTransform_):
    """
    StructureMapTransform

    How data is copied/created.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/map-transform
    """

    class Meta:
        resource = _resource
