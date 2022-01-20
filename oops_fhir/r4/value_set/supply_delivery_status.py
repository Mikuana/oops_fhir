from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.supply_delivery_status import (
    SupplyDeliveryStatus as SupplyDeliveryStatus_,
)


__all__ = ["SupplyDeliveryStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SupplyDeliveryStatus(SupplyDeliveryStatus_):
    """
    SupplyDeliveryStatus

    Status of the supply delivery.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/supplydelivery-status
    """

    class Meta:
        resource = _resource
