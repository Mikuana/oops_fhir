from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["InvoicePriceComponentType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class InvoicePriceComponentType:
    """
    InvoicePriceComponentType

    Codes indicating the kind of the price component.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/invoice-priceComponentType
    """

    base = CodeSystemConcept(
        {
            "code": "base",
            "definition": "the amount is the base price used for calculating the total price before applying surcharges, discount or taxes.",
            "display": "base price",
        }
    )
    """
    base price

    the amount is the base price used for calculating the total price before applying surcharges, discount or taxes.
    """

    surcharge = CodeSystemConcept(
        {
            "code": "surcharge",
            "definition": "the amount is a surcharge applied on the base price.",
            "display": "surcharge",
        }
    )
    """
    surcharge

    the amount is a surcharge applied on the base price.
    """

    deduction = CodeSystemConcept(
        {
            "code": "deduction",
            "definition": "the amount is a deduction applied on the base price.",
            "display": "deduction",
        }
    )
    """
    deduction

    the amount is a deduction applied on the base price.
    """

    discount = CodeSystemConcept(
        {
            "code": "discount",
            "definition": "the amount is a discount applied on the base price.",
            "display": "discount",
        }
    )
    """
    discount

    the amount is a discount applied on the base price.
    """

    tax = CodeSystemConcept(
        {
            "code": "tax",
            "definition": "the amount is the tax component of the total price.",
            "display": "tax",
        }
    )
    """
    tax

    the amount is the tax component of the total price.
    """

    informational = CodeSystemConcept(
        {
            "code": "informational",
            "definition": "the amount is of informational character, it has not been applied in the calculation of the total price.",
            "display": "informational",
        }
    )
    """
    informational

    the amount is of informational character, it has not been applied in the calculation of the total price.
    """

    class Meta:
        resource = _resource
