from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.organization_affiliation_role import (
    OrganizationAffiliationRole as OrganizationAffiliationRole_,
)


__all__ = ["OrganizationAffiliationRole"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class OrganizationAffiliationRole(OrganizationAffiliationRole_):
    """
    Organization Affiliation Role

    This example value set defines a set of codes that can be used to
indicate the role of one Organization in relation to another.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/organization-role
    """

    class Meta:
        resource = _resource
