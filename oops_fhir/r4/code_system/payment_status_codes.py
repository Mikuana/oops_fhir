from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["PaymentStatusCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class PaymentStatusCodes:
    """
    Payment Status Codes

    This value set includes a sample set of Payment Status codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/paymentstatus
    """

    paid = CodeSystemConcept(
        {
            "code": "paid",
            "definition": "The payment has been sent physically or electronically.",
            "display": "Paid",
        }
    )
    """
    Paid

    The payment has been sent physically or electronically.
    """

    cleared = CodeSystemConcept(
        {
            "code": "cleared",
            "definition": "The payment has been received by the payee.",
            "display": "Cleared",
        }
    )
    """
    Cleared

    The payment has been received by the payee.
    """

    class Meta:
        resource = _resource
