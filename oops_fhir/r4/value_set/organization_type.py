from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.organization_type import (
    OrganizationType as OrganizationType_,
)


__all__ = ["OrganizationType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class OrganizationType(OrganizationType_):
    """
    Organization type

    This example value set defines a set of codes that can be used to
indicate a type of organization.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/organization-type
    """

    class Meta:
        resource = _resource
