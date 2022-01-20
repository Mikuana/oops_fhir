from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MessageTransport"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MessageTransport:
    """
    MessageTransport

    The protocol used for message transport.

    Status: active - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/message-transport
    """

    http = CodeSystemConcept(
        {
            "code": "http",
            "definition": "The application sends or receives messages using HTTP POST (may be over http: or https:).",
            "display": "HTTP",
        }
    )
    """
    HTTP

    The application sends or receives messages using HTTP POST (may be over http: or https:).
    """

    ftp = CodeSystemConcept(
        {
            "code": "ftp",
            "definition": "The application sends or receives messages using File Transfer Protocol.",
            "display": "FTP",
        }
    )
    """
    FTP

    The application sends or receives messages using File Transfer Protocol.
    """

    mllp = CodeSystemConcept(
        {
            "code": "mllp",
            "definition": "The application sends or receives messages using HL7's Minimal Lower Level Protocol.",
            "display": "MLLP",
        }
    )
    """
    MLLP

    The application sends or receives messages using HL7's Minimal Lower Level Protocol.
    """

    class Meta:
        resource = _resource
