from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_role_class import v3RoleClass as v3RoleClass_


__all__ = ["v3RoleClass"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3RoleClass(v3RoleClass_):
    """
    v3 Code System RoleClass

     Codes for the Role class hierarchy.  The values in this hierarchy,
represent a Role which is an association or relationship between two
entities - the entity that plays the role and the entity that scopes the
role.  Roles names are derived from the name of the playing entity in
that role. The role hierarchy stems from three core concepts, or
abstract domains:    RoleClassOntological  is an abstract domain that
collects roles in which the playing entity is defined or specified by
the scoping entity.   RoleClassPartitive  collects roles in which the
playing entity is in some sense a "part" of the scoping entity.
RoleClassAssociative  collects all of the remaining forms of association
between the playing entity and the scoping entity. This set of roles is
further partitioned between:    RoleClassPassive  which are roles in
which the playing entity is used, known, treated, handled, built, or
destroyed, etc. under the auspices of the scoping entity. The playing
entity is passive in these roles in that the role exists without an
agreement from the playing entity.   RoleClassMutualRelationship  which
are relationships based on mutual behavior of the two entities. The
basis of these relationship may be formal agreements or they may bede
facto  behavior.  Thus, this sub-domain is further divided into:
RoleClassRelationshipFormal  in which the relationship is formally
defined, frequently by a contract or agreement.   Personal relationship
which inks two people in a personal relationship. The hierarchy
discussed above is represented In the current vocabulary tables as a set
of abstract domains, with the exception of the  "Personal relationship"
which is a leaf concept.  OpenIssue:  Description copied from Concept
Domain of same name.  Must be verified.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-RoleClass
    """

    class Meta:
        resource = _resource
