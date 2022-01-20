from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_role_class import v3RoleClass


__all__ = ["v3RoleClassAssociative"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3RoleClassAssociative(v3RoleClass):
    """
    V3 Value SetRoleClassAssociative

     A general association between two entities that is neither partitive
nor ontological.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-RoleClassAssociative
    """

    class Meta:
        resource = _resource
