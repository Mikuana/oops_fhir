from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AddressType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AddressType:
    """
    AddressType

    The type of an address (physical / postal).

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/address-type
    """

    postal = CodeSystemConcept(
        {
            "code": "postal",
            "definition": "Mailing addresses - PO Boxes and care-of addresses.",
            "display": "Postal",
        }
    )
    """
    Postal

    Mailing addresses - PO Boxes and care-of addresses.
    """

    physical = CodeSystemConcept(
        {
            "code": "physical",
            "definition": "A physical address that can be visited.",
            "display": "Physical",
        }
    )
    """
    Physical

    A physical address that can be visited.
    """

    both = CodeSystemConcept(
        {
            "code": "both",
            "definition": "An address that is both physical and postal.",
            "display": "Postal & Physical",
        }
    )
    """
    Postal & Physical

    An address that is both physical and postal.
    """

    class Meta:
        resource = _resource
