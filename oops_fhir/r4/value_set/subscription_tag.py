from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.subscription_tag import (
    SubscriptionTag as SubscriptionTag_,
)


__all__ = ["SubscriptionTag"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SubscriptionTag(SubscriptionTag_):
    """
    SubscriptionTag

    Tags to put on a resource after subscriptions have been sent.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/subscription-tag
    """

    class Meta:
        resource = _resource
