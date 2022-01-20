from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_specimen_type import v3SpecimenType as v3SpecimenType_


__all__ = ["v3SpecimenType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3SpecimenType(v3SpecimenType_):
    """
    v3 Code System SpecimenType

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-SpecimenType
    """

    class Meta:
        resource = _resource
