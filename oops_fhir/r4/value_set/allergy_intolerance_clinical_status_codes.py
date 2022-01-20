from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.allergy_intolerance_clinical_status_codes import (
    AllergyIntoleranceClinicalStatusCodes as AllergyIntoleranceClinicalStatusCodes_,
)


__all__ = ["AllergyIntoleranceClinicalStatusCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AllergyIntoleranceClinicalStatusCodes(AllergyIntoleranceClinicalStatusCodes_):
    """
    AllergyIntolerance Clinical Status Codes

    Preferred value set for AllergyIntolerance Clinical Status.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/allergyintolerance-clinical
    """

    class Meta:
        resource = _resource
