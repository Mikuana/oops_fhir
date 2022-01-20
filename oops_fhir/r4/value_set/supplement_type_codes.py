from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["SupplementTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SupplementTypeCodes(ValueSet):
    """
    Supplement Type Codes

    SupplementType :  Codes for nutritional supplements to be provided to
the patient. This value set is composed of SNOMED CT (US Extension)
Concepts from SCTID 470581016 (Enteral+supplement feeds hierarchy
(product)) and is provided as a suggestive example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/supplement-type
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
