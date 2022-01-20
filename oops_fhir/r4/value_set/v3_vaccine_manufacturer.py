from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_vaccine_manufacturer import (
    v3VaccineManufacturer as v3VaccineManufacturer_,
)


__all__ = ["v3VaccineManufacturer"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3VaccineManufacturer(v3VaccineManufacturer_):
    """
    v3 Code System VaccineManufacturer

     The manufacturer of a vaccine.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-VaccineManufacturer
    """

    class Meta:
        resource = _resource
