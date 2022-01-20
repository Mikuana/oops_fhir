from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExampleRelatedClaimRelationshipCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExampleRelatedClaimRelationshipCodes:
    """
    Example Related Claim Relationship Codes

    This value set includes sample Related Claim Relationship codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/ex-relatedclaimrelationship
    """

    prior = CodeSystemConcept(
        {
            "code": "prior",
            "definition": "A prior claim instance for the same intended suite of services.",
            "display": "Prior Claim",
        }
    )
    """
    Prior Claim

    A prior claim instance for the same intended suite of services.
    """

    associated = CodeSystemConcept(
        {
            "code": "associated",
            "definition": "A claim for a different suite of services which is related the suite claimed here.",
            "display": "Associated Claim",
        }
    )
    """
    Associated Claim

    A claim for a different suite of services which is related the suite claimed here.
    """

    class Meta:
        resource = _resource
