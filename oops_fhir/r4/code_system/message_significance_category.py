from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MessageSignificanceCategory"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MessageSignificanceCategory:
    """
    MessageSignificanceCategory

    The impact of the content of a message.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/message-significance-category
    """

    consequence = CodeSystemConcept(
        {
            "code": "consequence",
            "definition": "The message represents/requests a change that should not be processed more than once; e.g., making a booking for an appointment.",
            "display": "Consequence",
        }
    )
    """
    Consequence

    The message represents/requests a change that should not be processed more than once; e.g., making a booking for an appointment.
    """

    currency = CodeSystemConcept(
        {
            "code": "currency",
            "definition": "The message represents a response to query for current information. Retrospective processing is wrong and/or wasteful.",
            "display": "Currency",
        }
    )
    """
    Currency

    The message represents a response to query for current information. Retrospective processing is wrong and/or wasteful.
    """

    notification = CodeSystemConcept(
        {
            "code": "notification",
            "definition": "The content is not necessarily intended to be current, and it can be reprocessed, though there may be version issues created by processing old notifications.",
            "display": "Notification",
        }
    )
    """
    Notification

    The content is not necessarily intended to be current, and it can be reprocessed, though there may be version issues created by processing old notifications.
    """

    class Meta:
        resource = _resource
