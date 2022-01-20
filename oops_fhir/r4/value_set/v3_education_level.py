from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_education_level import (
    v3EducationLevel as v3EducationLevel_,
)


__all__ = ["v3EducationLevel"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EducationLevel(v3EducationLevel_):
    """
    v3 Code System EducationLevel

     Years of education that a person has completed

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-EducationLevel
    """

    class Meta:
        resource = _resource
