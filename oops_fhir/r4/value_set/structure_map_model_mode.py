from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.structure_map_model_mode import (
    StructureMapModelMode as StructureMapModelMode_,
)


__all__ = ["StructureMapModelMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class StructureMapModelMode(StructureMapModelMode_):
    """
    StructureMapModelMode

    How the referenced structure is used in this mapping.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/map-model-mode
    """

    class Meta:
        resource = _resource
