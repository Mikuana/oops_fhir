from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3CommunicationFunctionType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3CommunicationFunctionType:
    """
    v3 Code System CommunicationFunctionType

     Describes the type of communication function that the associated entity
plays in the associated transmission.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-CommunicationFunctionType
    """

    rcv = CodeSystemConcept(
        {
            "code": "RCV",
            "definition": "The entity is the receiver of the transmission.",
            "display": "receiver",
        }
    )
    """
    receiver

    The entity is the receiver of the transmission.
    """

    rsp = CodeSystemConcept(
        {
            "code": "RSP",
            "definition": "The entity is the one to which the response or reply to the transmission should be sent.",
            "display": "respond to",
        }
    )
    """
    respond to

    The entity is the one to which the response or reply to the transmission should be sent.
    """

    snd = CodeSystemConcept(
        {
            "code": "SND",
            "definition": "The entity is the sender of the transmission.",
            "display": "sender",
        }
    )
    """
    sender

    The entity is the sender of the transmission.
    """

    class Meta:
        resource = _resource
