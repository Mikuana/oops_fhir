from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.location_mode import LocationMode as LocationMode_


__all__ = ["LocationMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class LocationMode(LocationMode_):
    """
    LocationMode

    Indicates whether a resource instance represents a specific location or
a class of locations.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/location-mode
    """

    class Meta:
        resource = _resource
