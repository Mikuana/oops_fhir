from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_role_class import v3RoleClass


__all__ = ["v3RoleClassRelationshipFormal"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3RoleClassRelationshipFormal(v3RoleClass):
    """
    V3 Value SetRoleClassRelationshipFormal

     A relationship between two entities that is formally recognized,
frequently by a contract or similar agreement.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-RoleClassRelationshipFormal
    """

    class Meta:
        resource = _resource
