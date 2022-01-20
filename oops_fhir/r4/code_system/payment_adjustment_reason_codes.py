from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["PaymentAdjustmentReasonCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class PaymentAdjustmentReasonCodes:
    """
    Payment Adjustment Reason Codes

    This value set includes smattering of Payment Adjustment Reason codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/payment-adjustment-reason
    """

    a001 = CodeSystemConcept(
        {
            "code": "a001",
            "definition": "Prior Payment Reversal",
            "display": "Prior Payment Reversal",
        }
    )
    """
    Prior Payment Reversal

    Prior Payment Reversal
    """

    a002 = CodeSystemConcept(
        {
            "code": "a002",
            "definition": "Prior Overpayment",
            "display": "Prior Overpayment",
        }
    )
    """
    Prior Overpayment

    Prior Overpayment
    """

    class Meta:
        resource = _resource
