from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.supply_type import SupplyType as SupplyType_


__all__ = ["SupplyType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SupplyType(SupplyType_):
    """
    Supply Type

    This value sets refers to a Category of supply.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/supplyrequest-kind
    """

    class Meta:
        resource = _resource
