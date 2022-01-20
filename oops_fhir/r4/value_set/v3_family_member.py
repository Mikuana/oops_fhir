from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_role_code import v3RoleCode


__all__ = ["v3FamilyMember"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3FamilyMember(v3RoleCode):
    """
    V3 Value SetFamilyMember

     A relationship between two people characterizing their "familial"
relationship

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-FamilyMember
    """

    class Meta:
        resource = _resource
