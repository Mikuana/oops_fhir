from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.endpoint_payload_type import (
    EndpointPayloadType as EndpointPayloadType_,
)


__all__ = ["EndpointPayloadType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EndpointPayloadType(ValueSet):
    """
    Endpoint Payload Type

    This is an example value set defined by the FHIR project, that could be
used to represent possible payload document types.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/endpoint-payload-type
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
