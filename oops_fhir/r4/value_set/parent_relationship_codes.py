from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_role_code import v3RoleCode


__all__ = ["ParentRelationshipCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ParentRelationshipCodes(ValueSet):
    """
    Parent Relationship Codes

    The value set includes the v3 RoleCode PRN (parent), TWIN (twin) and all
of their specializations.  It covers the relationships needed to
establish genetic pedigree relationships between family members.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/parent-relationship-codes
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
