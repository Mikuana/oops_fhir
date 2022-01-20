from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AuditEventAgentNetworkType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AuditEventAgentNetworkType:
    """
    AuditEventAgentNetworkType

    The type of network access point of this agent in the audit event.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/network-type
    """

    one = CodeSystemConcept(
        {
            "code": "1",
            "definition": "The machine name, including DNS name.",
            "display": "Machine Name",
        }
    )
    """
    Machine Name

    The machine name, including DNS name.
    """

    two = CodeSystemConcept(
        {
            "code": "2",
            "definition": "The assigned Internet Protocol (IP) address.",
            "display": "IP Address",
        }
    )
    """
    IP Address

    The assigned Internet Protocol (IP) address.
    """

    three = CodeSystemConcept(
        {
            "code": "3",
            "definition": "The assigned telephone number.",
            "display": "Telephone Number",
        }
    )
    """
    Telephone Number

    The assigned telephone number.
    """

    four = CodeSystemConcept(
        {
            "code": "4",
            "definition": "The assigned email address.",
            "display": "Email address",
        }
    )
    """
    Email address

    The assigned email address.
    """

    five = CodeSystemConcept(
        {
            "code": "5",
            "definition": "URI (User directory, HTTP-PUT, ftp, etc.).",
            "display": "URI",
        }
    )
    """
    URI

    URI (User directory, HTTP-PUT, ftp, etc.).
    """

    class Meta:
        resource = _resource
