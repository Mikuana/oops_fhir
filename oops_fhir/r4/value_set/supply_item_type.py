from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.supply_item_type import SupplyItemType as SupplyItemType_


__all__ = ["SupplyItemType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SupplyItemType(SupplyItemType_):
    """
    Supply Item Type

    This value sets refers to a specific supply item.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/supplydelivery-type
    """

    class Meta:
        resource = _resource
