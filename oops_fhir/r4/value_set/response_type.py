from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.response_type import ResponseType as ResponseType_


__all__ = ["ResponseType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ResponseType(ResponseType_):
    """
    ResponseType

    The kind of response to a message.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/response-code
    """

    class Meta:
        resource = _resource
