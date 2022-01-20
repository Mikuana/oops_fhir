from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.example_payment_type_codes import (
    ExamplePaymentTypeCodes as ExamplePaymentTypeCodes_,
)


__all__ = ["ExamplePaymentTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExamplePaymentTypeCodes(ExamplePaymentTypeCodes_):
    """
    Example Payment Type Codes

    This value set includes example Payment Type codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/ex-paymenttype
    """

    class Meta:
        resource = _resource
