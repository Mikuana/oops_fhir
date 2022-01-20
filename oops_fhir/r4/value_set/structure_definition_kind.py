from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.structure_definition_kind import (
    StructureDefinitionKind as StructureDefinitionKind_,
)


__all__ = ["StructureDefinitionKind"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class StructureDefinitionKind(StructureDefinitionKind_):
    """
    StructureDefinitionKind

    Defines the type of structure that a definition is describing.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/structure-definition-kind
    """

    class Meta:
        resource = _resource
