from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.modifier_type_codes import (
    ModifierTypeCodes as ModifierTypeCodes_,
)


__all__ = ["ModifierTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ModifierTypeCodes(ModifierTypeCodes_):
    """
    Modifier type Codes

    This value set includes sample Modifier type codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/claim-modifiers
    """

    class Meta:
        resource = _resource
