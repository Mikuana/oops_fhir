from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.event_status import EventStatus as EventStatus_


__all__ = ["EventStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EventStatus(EventStatus_):
    """
    EventStatus

    Codes identifying the lifecycle stage of an event.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/event-status
    """

    class Meta:
        resource = _resource
