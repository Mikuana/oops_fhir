from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.address_type import AddressType as AddressType_


__all__ = ["AddressType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AddressType(AddressType_):
    """
    AddressType

    The type of an address (physical / postal).

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/address-type
    """

    class Meta:
        resource = _resource
