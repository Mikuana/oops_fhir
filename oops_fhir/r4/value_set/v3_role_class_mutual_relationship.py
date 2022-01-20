from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_role_class import v3RoleClass


__all__ = ["v3RoleClassMutualRelationship"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3RoleClassMutualRelationship(v3RoleClass):
    """
    V3 Value SetRoleClassMutualRelationship

     A relationship that is based on mutual behavior of the two Entities as
being related. The basis of such relationship may be agreements (e.g.,
spouses, contract parties) or they may bede facto  behavior (e.g.
friends) or may be an incidental involvement with each other (e.g.
parties over a dispute, siblings, children).

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-RoleClassMutualRelationship
    """

    class Meta:
        resource = _resource
