from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_role_class import v3RoleClass


__all__ = ["v3RoleClassPassive"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3RoleClassPassive(v3RoleClass):
    """
    V3 Value SetRoleClassPassive

     An association for a playing Entity that is used, known, treated,
handled, built, or destroyed, etc. under the auspices of the scoping
Entity. The playing Entity is passive in these roles (even though it may
be active in other roles), in the sense that the kinds of things done to
it in this role happen without an agreement from the playing Entity.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-RoleClassPassive
    """

    class Meta:
        resource = _resource
