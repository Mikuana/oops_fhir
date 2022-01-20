from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.definition_use_codes import (
    DefinitionUseCodes as DefinitionUseCodes_,
)


__all__ = ["DefinitionUseCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DefinitionUseCodes(DefinitionUseCodes_):
    """
    Structure Definition Use Codes / Keywords

    Structure Definition Use Codes / Keywords

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/definition-use
    """

    class Meta:
        resource = _resource
