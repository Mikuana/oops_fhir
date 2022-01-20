from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.care_team_status import CareTeamStatus as CareTeamStatus_


__all__ = ["CareTeamStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CareTeamStatus(CareTeamStatus_):
    """
    CareTeamStatus

    Indicates the status of the care team.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/care-team-status
    """

    class Meta:
        resource = _resource
