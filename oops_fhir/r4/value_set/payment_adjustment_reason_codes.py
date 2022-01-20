from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.payment_adjustment_reason_codes import (
    PaymentAdjustmentReasonCodes as PaymentAdjustmentReasonCodes_,
)


__all__ = ["PaymentAdjustmentReasonCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class PaymentAdjustmentReasonCodes(PaymentAdjustmentReasonCodes_):
    """
    Payment Adjustment Reason Codes

    This value set includes smattering of Payment Adjustment Reason codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/payment-adjustment-reason
    """

    class Meta:
        resource = _resource
