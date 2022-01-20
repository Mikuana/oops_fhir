from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_address_part_type import (
    v3AddressPartType as v3AddressPartType_,
)


__all__ = ["v3AddressPartType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3AddressPartType(v3AddressPartType_):
    """
    v3 Code System AddressPartType

      Description:  Code that specifies whether an address part names the
street, city, country, postal code, post box, etc. Discussion: The
hierarchical nature of these concepts shows composition.  E.g. "Street
Name" is part of "Street Address Line"

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-AddressPartType
    """

    class Meta:
        resource = _resource
