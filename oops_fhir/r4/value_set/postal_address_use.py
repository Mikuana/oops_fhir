from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["PostalAddressUse"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class PostalAddressUse(ValueSet):
    """
    PostalAddressUse

    Uses of an address not included in Address.use.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/postal-address-use
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
