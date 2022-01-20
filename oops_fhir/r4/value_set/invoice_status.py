from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.invoice_status import InvoiceStatus as InvoiceStatus_


__all__ = ["InvoiceStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class InvoiceStatus(InvoiceStatus_):
    """
    InvoiceStatus

    Codes identifying the lifecycle stage of an Invoice.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/invoice-status
    """

    class Meta:
        resource = _resource
