from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.endpoint_status import EndpointStatus as EndpointStatus_


__all__ = ["EndpointStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EndpointStatus(EndpointStatus_):
    """
    EndpointStatus

    The status of the endpoint.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/endpoint-status
    """

    class Meta:
        resource = _resource
