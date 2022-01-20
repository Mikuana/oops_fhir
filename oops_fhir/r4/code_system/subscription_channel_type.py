from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SubscriptionChannelType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SubscriptionChannelType:
    """
    SubscriptionChannelType

    The type of method used to execute a subscription.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/subscription-channel-type
    """

    rest_hook = CodeSystemConcept(
        {
            "code": "rest-hook",
            "definition": "The channel is executed by making a post to the URI. If a payload is included, the URL is interpreted as the service base, and an update (PUT) is made.",
            "display": "Rest Hook",
        }
    )
    """
    Rest Hook

    The channel is executed by making a post to the URI. If a payload is included, the URL is interpreted as the service base, and an update (PUT) is made.
    """

    websocket = CodeSystemConcept(
        {
            "code": "websocket",
            "definition": "The channel is executed by sending a packet across a web socket connection maintained by the client. The URL identifies the websocket, and the client binds to this URL.",
            "display": "Websocket",
        }
    )
    """
    Websocket

    The channel is executed by sending a packet across a web socket connection maintained by the client. The URL identifies the websocket, and the client binds to this URL.
    """

    email = CodeSystemConcept(
        {
            "code": "email",
            "definition": "The channel is executed by sending an email to the email addressed in the URI (which must be a mailto:).",
            "display": "Email",
        }
    )
    """
    Email

    The channel is executed by sending an email to the email addressed in the URI (which must be a mailto:).
    """

    sms = CodeSystemConcept(
        {
            "code": "sms",
            "definition": "The channel is executed by sending an SMS message to the phone number identified in the URL (tel:).",
            "display": "SMS",
        }
    )
    """
    SMS

    The channel is executed by sending an SMS message to the phone number identified in the URL (tel:).
    """

    message = CodeSystemConcept(
        {
            "code": "message",
            "definition": "The channel is executed by sending a message (e.g. a Bundle with a MessageHeader resource etc.) to the application identified in the URI.",
            "display": "Message",
        }
    )
    """
    Message

    The channel is executed by sending a message (e.g. a Bundle with a MessageHeader resource etc.) to the application identified in the URI.
    """

    class Meta:
        resource = _resource
