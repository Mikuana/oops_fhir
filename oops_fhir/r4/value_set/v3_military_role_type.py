from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_role_code import v3RoleCode


__all__ = ["v3MilitaryRoleType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3MilitaryRoleType(v3RoleCode):
    """
    V3 Value SetMilitaryRoleType

      Definition:  A person playing the role of program eligible under a
program based on military status.  Discussion:  This
CoveredPartyRoleType.code is typically used when the CoveredPartyRole
class code is either "program eligible" or "subscriber" and the person's
status as a member of the military meets jurisdictional or program
criteria

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-MilitaryRoleType
    """

    class Meta:
        resource = _resource
