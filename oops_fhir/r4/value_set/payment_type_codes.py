from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.payment_type_codes import (
    PaymentTypeCodes as PaymentTypeCodes_,
)


__all__ = ["PaymentTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class PaymentTypeCodes(PaymentTypeCodes_):
    """
    Payment Type Codes

    This value set includes sample Payment Type codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/payment-type
    """

    class Meta:
        resource = _resource
