from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.allergy_intolerance_type import (
    AllergyIntoleranceType as AllergyIntoleranceType_,
)


__all__ = ["AllergyIntoleranceType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AllergyIntoleranceType(AllergyIntoleranceType_):
    """
    AllergyIntoleranceType

    Identification of the underlying physiological mechanism for a Reaction
Risk.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/allergy-intolerance-type
    """

    class Meta:
        resource = _resource
