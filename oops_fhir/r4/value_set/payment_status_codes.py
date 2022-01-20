from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.payment_status_codes import (
    PaymentStatusCodes as PaymentStatusCodes_,
)


__all__ = ["PaymentStatusCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class PaymentStatusCodes(PaymentStatusCodes_):
    """
    Payment Status Codes

    This value set includes a sample set of Payment Status codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/payment-status
    """

    class Meta:
        resource = _resource
