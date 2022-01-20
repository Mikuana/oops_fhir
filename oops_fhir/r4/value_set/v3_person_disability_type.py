from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_person_disability_type import (
    v3PersonDisabilityType as v3PersonDisabilityType_,
)


__all__ = ["v3PersonDisabilityType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3PersonDisabilityType(v3PersonDisabilityType_):
    """
    v3 Code System PersonDisabilityType

     A code identifying a person's disability.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-PersonDisabilityType
    """

    class Meta:
        resource = _resource
