from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AddressUse"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AddressUse:
    """
    AddressUse

    The use of an address.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/address-use
    """

    home = CodeSystemConcept(
        {
            "code": "home",
            "definition": "A communication address at a home.",
            "display": "Home",
        }
    )
    """
    Home

    A communication address at a home.
    """

    work = CodeSystemConcept(
        {
            "code": "work",
            "definition": "An office address. First choice for business related contacts during business hours.",
            "display": "Work",
        }
    )
    """
    Work

    An office address. First choice for business related contacts during business hours.
    """

    temp = CodeSystemConcept(
        {
            "code": "temp",
            "definition": "A temporary address. The period can provide more detailed information.",
            "display": "Temporary",
        }
    )
    """
    Temporary

    A temporary address. The period can provide more detailed information.
    """

    old = CodeSystemConcept(
        {
            "code": "old",
            "definition": "This address is no longer in use (or was never correct but retained for records).",
            "display": "Old / Incorrect",
        }
    )
    """
    Old / Incorrect

    This address is no longer in use (or was never correct but retained for records).
    """

    billing = CodeSystemConcept(
        {
            "code": "billing",
            "definition": "An address to be used to send bills, invoices, receipts etc.",
            "display": "Billing",
        }
    )
    """
    Billing

    An address to be used to send bills, invoices, receipts etc.
    """

    class Meta:
        resource = _resource
