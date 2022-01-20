from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.service_type import ServiceType as ServiceType_


__all__ = ["ServiceType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ServiceType(ServiceType_):
    """
    Service type

    This value set defines an example set of codes of service-types.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/service-type
    """

    class Meta:
        resource = _resource
