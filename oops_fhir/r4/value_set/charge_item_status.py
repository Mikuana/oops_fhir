from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.charge_item_status import (
    ChargeItemStatus as ChargeItemStatus_,
)


__all__ = ["ChargeItemStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ChargeItemStatus(ChargeItemStatus_):
    """
    ChargeItemStatus

    Codes identifying the lifecycle stage of a ChargeItem.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/chargeitem-status
    """

    class Meta:
        resource = _resource
