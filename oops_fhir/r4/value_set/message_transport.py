from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.message_transport import (
    MessageTransport as MessageTransport_,
)


__all__ = ["MessageTransport"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MessageTransport(MessageTransport_):
    """
    MessageTransport

    The protocol used for message transport.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/message-transport
    """

    class Meta:
        resource = _resource
