from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.resource_security_category import (
    ResourceSecurityCategory as ResourceSecurityCategory_,
)


__all__ = ["ResourceSecurityCategory"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ResourceSecurityCategory(ResourceSecurityCategory_):
    """
    ResourceSecurityCategory

    Provides general guidance around the kind of access Control to Read,
Search, Create, Update, or Delete a resource.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/resource-security-category
    """

    class Meta:
        resource = _resource
