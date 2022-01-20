from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.resource_version_policy import (
    ResourceVersionPolicy as ResourceVersionPolicy_,
)


__all__ = ["ResourceVersionPolicy"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ResourceVersionPolicy(ResourceVersionPolicy_):
    """
    ResourceVersionPolicy

    How the system supports versioning for a resource.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/versioning-policy
    """

    class Meta:
        resource = _resource
