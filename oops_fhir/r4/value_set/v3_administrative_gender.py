from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_administrative_gender import (
    v3AdministrativeGender as v3AdministrativeGender_,
)


__all__ = ["v3AdministrativeGender"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3AdministrativeGender(v3AdministrativeGender_):
    """
    v3 Code System AdministrativeGender

     The gender of a person used for adminstrative purposes (as opposed to
clinical gender)

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-AdministrativeGender
    """

    class Meta:
        resource = _resource
