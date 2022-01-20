from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["EnteralFormulaTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EnteralFormulaTypeCodes(ValueSet):
    """
    Enteral Formula Type Codes

    EnteralFormulaType : Codes for type of enteral formula to be
administered to patient.  This value set is composed of SNOMED CT (US
Extension) Concepts from SCTID 470581016 (Enteral+supplement feeds
hierarchy (product)) and is provided as a suggestive example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/entformula-type
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
