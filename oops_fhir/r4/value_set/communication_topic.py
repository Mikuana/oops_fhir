from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.communication_topic import (
    CommunicationTopic as CommunicationTopic_,
)


__all__ = ["CommunicationTopic"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CommunicationTopic(CommunicationTopic_):
    """
    CommunicationTopic

    Codes describing the purpose or content of the communication.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/communication-topic
    """

    class Meta:
        resource = _resource
