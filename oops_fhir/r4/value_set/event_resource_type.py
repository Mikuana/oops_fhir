from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.event_resource_type import (
    EventResourceType as EventResourceType_,
)


__all__ = ["EventResourceType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EventResourceType(EventResourceType_):
    """
    EventResourceType

    A list of all the event resource types defined in this version of the
FHIR specification.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/event-resource-types
    """

    class Meta:
        resource = _resource
