from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ClaimCareTeamRoleCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ClaimCareTeamRoleCodes:
    """
    Claim Care Team Role Codes

    This value set includes sample Claim Care Team Role codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/claimcareteamrole
    """

    primary = CodeSystemConcept(
        {
            "code": "primary",
            "definition": "The primary care provider.",
            "display": "Primary provider",
        }
    )
    """
    Primary provider

    The primary care provider.
    """

    assist = CodeSystemConcept(
        {
            "code": "assist",
            "definition": "Assisting care provider.",
            "display": "Assisting Provider",
        }
    )
    """
    Assisting Provider

    Assisting care provider.
    """

    supervisor = CodeSystemConcept(
        {
            "code": "supervisor",
            "definition": "Supervising care provider.",
            "display": "Supervising Provider",
        }
    )
    """
    Supervising Provider

    Supervising care provider.
    """

    other = CodeSystemConcept(
        {
            "code": "other",
            "definition": "Other role on the care team.",
            "display": "Other",
        }
    )
    """
    Other

    Other role on the care team.
    """

    class Meta:
        resource = _resource
