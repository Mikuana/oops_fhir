from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.subscriber_relationship_codes import (
    SubscriberRelationshipCodes as SubscriberRelationshipCodes_,
)


__all__ = ["SubscriberRelationshipCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SubscriberRelationshipCodes(SubscriberRelationshipCodes_):
    """
    SubscriberPolicyholder Relationship Codes

    This value set includes codes for the relationship between the
Subscriber and the Beneficiary (insured/covered party/patient).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/subscriber-relationship
    """

    class Meta:
        resource = _resource
