from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SubscriptionTag"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SubscriptionTag:
    """
    SubscriptionTag

    Tags to put on a resource after subscriptions have been sent.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/subscription-tag
    """

    queued = CodeSystemConcept(
        {
            "code": "queued",
            "definition": "The message has been queued for processing on a destination systems.",
            "display": "Queued",
        }
    )
    """
    Queued

    The message has been queued for processing on a destination systems.
    """

    delivered = CodeSystemConcept(
        {
            "code": "delivered",
            "definition": "The message has been delivered to its intended recipient.",
            "display": "Delivered",
        }
    )
    """
    Delivered

    The message has been delivered to its intended recipient.
    """

    class Meta:
        resource = _resource
