from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.structure_map_context_type import (
    StructureMapContextType as StructureMapContextType_,
)


__all__ = ["StructureMapContextType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class StructureMapContextType(StructureMapContextType_):
    """
    StructureMapContextType

    How to interpret the context.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/map-context-type
    """

    class Meta:
        resource = _resource
