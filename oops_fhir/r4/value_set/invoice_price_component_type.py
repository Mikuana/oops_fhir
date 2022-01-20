from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.invoice_price_component_type import (
    InvoicePriceComponentType as InvoicePriceComponentType_,
)


__all__ = ["InvoicePriceComponentType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class InvoicePriceComponentType(InvoicePriceComponentType_):
    """
    InvoicePriceComponentType

    Codes indicating the kind of the price component.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/invoice-priceComponentType
    """

    class Meta:
        resource = _resource
