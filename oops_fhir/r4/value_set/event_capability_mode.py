from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.event_capability_mode import (
    EventCapabilityMode as EventCapabilityMode_,
)


__all__ = ["EventCapabilityMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EventCapabilityMode(EventCapabilityMode_):
    """
    EventCapabilityMode

    The mode of a message capability statement.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/event-capability-mode
    """

    class Meta:
        resource = _resource
