from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.oral_prostho_material_type_codes import (
    OralProsthoMaterialTypeCodes as OralProsthoMaterialTypeCodes_,
)


__all__ = ["OralProsthoMaterialTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class OralProsthoMaterialTypeCodes(OralProsthoMaterialTypeCodes_):
    """
    Oral Prostho Material type Codes

    This value set includes sample Oral Prosthodontic Material type codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/oral-prosthodontic-material
    """

    class Meta:
        resource = _resource
