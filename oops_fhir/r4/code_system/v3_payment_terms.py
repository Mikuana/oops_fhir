from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3PaymentTerms"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3PaymentTerms:
    """
    v3 Code System PaymentTerms

     Describes payment terms for a financial transaction, used in an
invoice. This is typically expressed as a responsibility of the acceptor
or payor of an invoice.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-PaymentTerms
    """

    cod = CodeSystemConcept(
        {
            "code": "COD",
            "definition": "Payment in full for products and/or services is required as soon as the service is performed or goods delivered.",
            "display": "Cash on Delivery",
        }
    )
    """
    Cash on Delivery

    Payment in full for products and/or services is required as soon as the service is performed or goods delivered.
    """

    n30 = CodeSystemConcept(
        {
            "code": "N30",
            "definition": "Payment in full for products and/or services is required 30 days from the time the service is performed or goods delivered.",
            "display": "Net 30 days",
        }
    )
    """
    Net 30 days

    Payment in full for products and/or services is required 30 days from the time the service is performed or goods delivered.
    """

    n60 = CodeSystemConcept(
        {
            "code": "N60",
            "definition": "Payment in full for products and/or services is required 60 days from the time the service is performed or goods delivered.",
            "display": "Net 60 days",
        }
    )
    """
    Net 60 days

    Payment in full for products and/or services is required 60 days from the time the service is performed or goods delivered.
    """

    n90 = CodeSystemConcept(
        {
            "code": "N90",
            "definition": "Payment in full for products and/or services is required 90 days from the time the service is performed or goods delivered.",
            "display": "Net 90 days",
        }
    )
    """
    Net 90 days

    Payment in full for products and/or services is required 90 days from the time the service is performed or goods delivered.
    """

    class Meta:
        resource = _resource
