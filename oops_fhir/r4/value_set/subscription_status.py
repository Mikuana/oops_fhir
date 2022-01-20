from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.subscription_status import (
    SubscriptionStatus as SubscriptionStatus_,
)


__all__ = ["SubscriptionStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SubscriptionStatus(SubscriptionStatus_):
    """
    SubscriptionStatus

    The status of a subscription.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/subscription-status
    """

    class Meta:
        resource = _resource
