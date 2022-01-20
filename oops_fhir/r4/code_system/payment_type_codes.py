from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["PaymentTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class PaymentTypeCodes:
    """
    Payment Type Codes

    This value set includes sample Payment Type codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/payment-type
    """

    payment = CodeSystemConcept(
        {
            "code": "payment",
            "definition": "The amount is partial or complete settlement of the amounts due.",
            "display": "Payment",
        }
    )
    """
    Payment

    The amount is partial or complete settlement of the amounts due.
    """

    adjustment = CodeSystemConcept(
        {
            "code": "adjustment",
            "definition": "The amount is an adjustment regarding claims already paid.",
            "display": "Adjustment",
        }
    )
    """
    Adjustment

    The amount is an adjustment regarding claims already paid.
    """

    advance = CodeSystemConcept(
        {
            "code": "advance",
            "definition": "The amount is an advance against future claims.",
            "display": "Advance",
        }
    )
    """
    Advance

    The amount is an advance against future claims.
    """

    class Meta:
        resource = _resource
