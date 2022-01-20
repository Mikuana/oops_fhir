from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CommunicationCategory"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CommunicationCategory:
    """
    CommunicationCategory

    Codes for general categories of communications such as alerts,
instructions, etc.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/communication-category
    """

    alert = CodeSystemConcept(
        {
            "code": "alert",
            "definition": "The communication conveys an alert.",
            "display": "Alert",
        }
    )
    """
    Alert

    The communication conveys an alert.
    """

    notification = CodeSystemConcept(
        {
            "code": "notification",
            "definition": "The communication conveys a notification.",
            "display": "Notification",
        }
    )
    """
    Notification

    The communication conveys a notification.
    """

    reminder = CodeSystemConcept(
        {
            "code": "reminder",
            "definition": "The communication conveys a reminder.",
            "display": "Reminder",
        }
    )
    """
    Reminder

    The communication conveys a reminder.
    """

    instruction = CodeSystemConcept(
        {
            "code": "instruction",
            "definition": "The communication conveys an instruction.",
            "display": "Instruction",
        }
    )
    """
    Instruction

    The communication conveys an instruction.
    """

    class Meta:
        resource = _resource
