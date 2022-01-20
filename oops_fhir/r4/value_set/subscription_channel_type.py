from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.subscription_channel_type import (
    SubscriptionChannelType as SubscriptionChannelType_,
)


__all__ = ["SubscriptionChannelType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SubscriptionChannelType(SubscriptionChannelType_):
    """
    SubscriptionChannelType

    The type of method used to execute a subscription.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/subscription-channel-type
    """

    class Meta:
        resource = _resource
