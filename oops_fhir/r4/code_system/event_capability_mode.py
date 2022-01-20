from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["EventCapabilityMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class EventCapabilityMode:
    """
    EventCapabilityMode

    The mode of a message capability statement.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/event-capability-mode
    """

    sender = CodeSystemConcept(
        {
            "code": "sender",
            "definition": "The application sends requests and receives responses.",
            "display": "Sender",
        }
    )
    """
    Sender

    The application sends requests and receives responses.
    """

    receiver = CodeSystemConcept(
        {
            "code": "receiver",
            "definition": "The application receives requests and sends responses.",
            "display": "Receiver",
        }
    )
    """
    Receiver

    The application receives requests and sends responses.
    """

    class Meta:
        resource = _resource
