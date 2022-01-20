from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.claim_processing_codes import (
    ClaimProcessingCodes as ClaimProcessingCodes_,
)


__all__ = ["ClaimProcessingCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ClaimProcessingCodes(ClaimProcessingCodes_):
    """
    Claim Processing Codes

    This value set includes Claim Processing Outcome codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/remittance-outcome
    """

    class Meta:
        resource = _resource
