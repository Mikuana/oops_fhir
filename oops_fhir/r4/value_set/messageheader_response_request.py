from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.messageheader_response_request import (
    messageheaderresponserequest as messageheaderresponserequest_,
)


__all__ = ["messageheaderresponserequest"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class messageheaderresponserequest(messageheaderresponserequest_):
    """
    messageheader-response-request

    HL7-defined table of codes which identify conditions under which
acknowledgments are required to be returned in response to a message.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/messageheader-response-request
    """

    class Meta:
        resource = _resource
