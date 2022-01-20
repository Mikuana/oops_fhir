from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_role_class import v3RoleClass


__all__ = ["v3RoleClassPartitive"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3RoleClassPartitive(v3RoleClass):
    """
    V3 Value SetRoleClassPartitive

     An association between two Entities where the playing Entity is
considered in some way "part" of the scoping Entity, e.g., as a member,
component, ingredient, or content. Being "part" in the broadest sense of
the word can mean anything from being an integral structural component
to a mere incidental temporary association of a playing Entity with a
(generally larger) scoping Entity.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-RoleClassPartitive
    """

    class Meta:
        resource = _resource
