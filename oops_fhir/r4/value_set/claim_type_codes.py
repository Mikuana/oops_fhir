from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.claim_type_codes import ClaimTypeCodes as ClaimTypeCodes_


__all__ = ["ClaimTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ClaimTypeCodes(ClaimTypeCodes_):
    """
    Claim Type Codes

    This value set includes Claim Type codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/claim-type
    """

    class Meta:
        resource = _resource
