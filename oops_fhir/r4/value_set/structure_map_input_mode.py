from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.structure_map_input_mode import (
    StructureMapInputMode as StructureMapInputMode_,
)


__all__ = ["StructureMapInputMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class StructureMapInputMode(StructureMapInputMode_):
    """
    StructureMapInputMode

    Mode for this instance of data.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/map-input-mode
    """

    class Meta:
        resource = _resource
