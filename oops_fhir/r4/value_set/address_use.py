from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.address_use import AddressUse as AddressUse_


__all__ = ["AddressUse"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AddressUse(AddressUse_):
    """
    AddressUse

    The use of an address.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/address-use
    """

    class Meta:
        resource = _resource
