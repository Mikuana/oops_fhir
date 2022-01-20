from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.enteral_formula_additive_type_code import (
    EnteralFormulaAdditiveTypeCode as EnteralFormulaAdditiveTypeCode_,
)


__all__ = ["EnteralFormulaAdditiveTypeCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EnteralFormulaAdditiveTypeCode(EnteralFormulaAdditiveTypeCode_):
    """
    Enteral Formula Additive Type Code

    EnteralFormulaAdditiveType: Codes for the type of modular component such
as protein, carbohydrate or fiber to be provided in addition to or mixed
with the base formula. This value set is provided as a suggestive
example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/entformula-additive
    """

    class Meta:
        resource = _resource
