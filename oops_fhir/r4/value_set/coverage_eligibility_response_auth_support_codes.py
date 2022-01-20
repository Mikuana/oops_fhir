from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.coverage_eligibility_response_auth_support_codes import (
    CoverageEligibilityResponseAuthSupportCodes as CoverageEligibilityResponseAuthSupportCodes_,
)


__all__ = ["CoverageEligibilityResponseAuthSupportCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CoverageEligibilityResponseAuthSupportCodes(
    CoverageEligibilityResponseAuthSupportCodes_
):
    """
    CoverageEligibilityResponse Auth Support Codes

    This value set includes CoverageEligibilityResponse Auth Support codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/coverageeligibilityresponse-ex-auth-support
    """

    class Meta:
        resource = _resource
