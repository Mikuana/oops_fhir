from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.example_related_claim_relationship_codes import (
    ExampleRelatedClaimRelationshipCodes as ExampleRelatedClaimRelationshipCodes_,
)


__all__ = ["ExampleRelatedClaimRelationshipCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExampleRelatedClaimRelationshipCodes(ExampleRelatedClaimRelationshipCodes_):
    """
    Example Related Claim Relationship Codes

    This value set includes sample Related Claim Relationship codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/related-claim-relationship
    """

    class Meta:
        resource = _resource
