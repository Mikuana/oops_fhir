from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_address_use import v3AddressUse as v3AddressUse_


__all__ = ["v3AddressUse"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3AddressUse(v3AddressUse_):
    """
    v3 Code System AddressUse

     Codes that provide guidance around the circumstances in which a given
address should be used.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-AddressUse
    """

    class Meta:
        resource = _resource
