from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.additional_material_codes import (
    AdditionalMaterialCodes as AdditionalMaterialCodes_,
)


__all__ = ["AdditionalMaterialCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AdditionalMaterialCodes(AdditionalMaterialCodes_):
    """
    Additional Material Codes

    This value set includes sample additional material type codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/additionalmaterials
    """

    class Meta:
        resource = _resource
