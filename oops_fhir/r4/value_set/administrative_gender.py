from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.administrative_gender import (
    AdministrativeGender as AdministrativeGender_,
)


__all__ = ["AdministrativeGender"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AdministrativeGender(AdministrativeGender_):
    """
    AdministrativeGender

    The gender of a person used for administrative purposes.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/administrative-gender
    """

    class Meta:
        resource = _resource
