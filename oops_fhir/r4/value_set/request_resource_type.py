from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.request_resource_type import (
    RequestResourceType as RequestResourceType_,
)


__all__ = ["RequestResourceType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class RequestResourceType(RequestResourceType_):
    """
    RequestResourceType

    A list of all the request resource types defined in this version of the
FHIR specification.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/request-resource-types
    """

    class Meta:
        resource = _resource
