from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.definition_resource_type import (
    DefinitionResourceType as DefinitionResourceType_,
)


__all__ = ["DefinitionResourceType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DefinitionResourceType(DefinitionResourceType_):
    """
    DefinitionResourceType

    A list of all the definition resource types defined in this version of
the FHIR specification.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/definition-resource-types
    """

    class Meta:
        resource = _resource
