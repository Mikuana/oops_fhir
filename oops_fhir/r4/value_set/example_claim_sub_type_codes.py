from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.example_claim_sub_type_codes import (
    ExampleClaimSubTypeCodes as ExampleClaimSubTypeCodes_,
)


__all__ = ["ExampleClaimSubTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExampleClaimSubTypeCodes(ExampleClaimSubTypeCodes_):
    """
    Example Claim SubType Codes

    This value set includes sample Claim SubType codes which are used to
distinguish the claim types for example within type institutional there
may be subtypes for emergency services, bed stay and transportation.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/claim-subtype
    """

    class Meta:
        resource = _resource
