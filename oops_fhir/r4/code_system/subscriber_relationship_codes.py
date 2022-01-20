from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SubscriberRelationshipCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SubscriberRelationshipCodes:
    """
    SubscriberPolicyholder Relationship Codes

    This value set includes codes for the relationship between the
Subscriber and the Beneficiary (insured/covered party/patient).

    Status: draft - Version: 4.0.1

    Copyright This is an extensible set.

    http://terminology.hl7.org/CodeSystem/subscriber-relationship
    """

    child = CodeSystemConcept(
        {
            "code": "child",
            "definition": "The Beneficiary is a child of the Subscriber",
            "display": "Child",
        }
    )
    """
    Child

    The Beneficiary is a child of the Subscriber
    """

    parent = CodeSystemConcept(
        {
            "code": "parent",
            "definition": "The Beneficiary is a parent of the Subscriber",
            "display": "Parent",
        }
    )
    """
    Parent

    The Beneficiary is a parent of the Subscriber
    """

    spouse = CodeSystemConcept(
        {
            "code": "spouse",
            "definition": "The Beneficiary is a spouse or equivalent of the Subscriber",
            "display": "Spouse",
        }
    )
    """
    Spouse

    The Beneficiary is a spouse or equivalent of the Subscriber
    """

    common = CodeSystemConcept(
        {
            "code": "common",
            "definition": "The Beneficiary is a common law spouse or equivalent of the Subscriber",
            "display": "Common Law Spouse",
        }
    )
    """
    Common Law Spouse

    The Beneficiary is a common law spouse or equivalent of the Subscriber
    """

    other = CodeSystemConcept(
        {
            "code": "other",
            "definition": "The Beneficiary has some other relationship the Subscriber",
            "display": "Other",
        }
    )
    """
    Other

    The Beneficiary has some other relationship the Subscriber
    """

    self = CodeSystemConcept(
        {
            "code": "self",
            "definition": "The Beneficiary is the Subscriber",
            "display": "Self",
        }
    )
    """
    Self

    The Beneficiary is the Subscriber
    """

    injured = CodeSystemConcept(
        {
            "code": "injured",
            "definition": "The Beneficiary is covered under insurance of the subscriber due to an injury.",
            "display": "Injured Party",
        }
    )
    """
    Injured Party

    The Beneficiary is covered under insurance of the subscriber due to an injury.
    """

    class Meta:
        resource = _resource
