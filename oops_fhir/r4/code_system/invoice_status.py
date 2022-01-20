from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["InvoiceStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class InvoiceStatus:
    """
    InvoiceStatus

    Codes identifying the lifecycle stage of an Invoice.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/invoice-status
    """

    draft = CodeSystemConcept(
        {
            "code": "draft",
            "definition": "the invoice has been prepared but not yet finalized.",
            "display": "draft",
        }
    )
    """
    draft

    the invoice has been prepared but not yet finalized.
    """

    issued = CodeSystemConcept(
        {
            "code": "issued",
            "definition": "the invoice has been finalized and sent to the recipient.",
            "display": "issued",
        }
    )
    """
    issued

    the invoice has been finalized and sent to the recipient.
    """

    balanced = CodeSystemConcept(
        {
            "code": "balanced",
            "definition": "the invoice has been balaced / completely paid.",
            "display": "balanced",
        }
    )
    """
    balanced

    the invoice has been balaced / completely paid.
    """

    cancelled = CodeSystemConcept(
        {
            "code": "cancelled",
            "definition": "the invoice was cancelled.",
            "display": "cancelled",
        }
    )
    """
    cancelled

    the invoice was cancelled.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "the invoice was determined as entered in error before it was issued.",
            "display": "entered in error",
        }
    )
    """
    entered in error

    the invoice was determined as entered in error before it was issued.
    """

    class Meta:
        resource = _resource
