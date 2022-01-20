from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.endpoint_connection_type import (
    EndpointConnectionType as EndpointConnectionType_,
)


__all__ = ["EndpointConnectionType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EndpointConnectionType(EndpointConnectionType_):
    """
    Endpoint Connection Type

    This is an example value set defined by the FHIR project, that could be
used to represent possible connection type profile values.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/endpoint-connection-type
    """

    class Meta:
        resource = _resource
