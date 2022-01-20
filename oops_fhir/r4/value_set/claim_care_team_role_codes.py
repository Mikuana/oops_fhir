from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.claim_care_team_role_codes import (
    ClaimCareTeamRoleCodes as ClaimCareTeamRoleCodes_,
)


__all__ = ["ClaimCareTeamRoleCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ClaimCareTeamRoleCodes(ClaimCareTeamRoleCodes_):
    """
    Claim Care Team Role Codes

    This value set includes sample Claim Care Team Role codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/claim-careteamrole
    """

    class Meta:
        resource = _resource
