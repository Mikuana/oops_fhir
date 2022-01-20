from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.charge_item_code import ChargeItemCode as ChargeItemCode_


__all__ = ["ChargeItemCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ChargeItemCode(ChargeItemCode_):
    """
    ChargeItemCode

    Example set of codes that can be used for billing purposes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/chargeitem-billingcodes
    """

    class Meta:
        resource = _resource
