from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SubscriptionStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SubscriptionStatus:
    """
    SubscriptionStatus

    The status of a subscription.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/subscription-status
    """

    requested = CodeSystemConcept(
        {
            "code": "requested",
            "definition": "The client has requested the subscription, and the server has not yet set it up.",
            "display": "Requested",
        }
    )
    """
    Requested

    The client has requested the subscription, and the server has not yet set it up.
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "The subscription is active.",
            "display": "Active",
        }
    )
    """
    Active

    The subscription is active.
    """

    error = CodeSystemConcept(
        {
            "code": "error",
            "definition": "The server has an error executing the notification.",
            "display": "Error",
        }
    )
    """
    Error

    The server has an error executing the notification.
    """

    off = CodeSystemConcept(
        {
            "code": "off",
            "definition": "Too many errors have occurred or the subscription has expired.",
            "display": "Off",
        }
    )
    """
    Off

    Too many errors have occurred or the subscription has expired.
    """

    class Meta:
        resource = _resource
