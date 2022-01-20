from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["EventOrRequestResourceTypes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EventOrRequestResourceTypes(ValueSet):
    """
    EventOrRequestResourceTypes

    This value set lists all the event or request resource types defined in
this version of the specification.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/event-or-request-resource-types
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
