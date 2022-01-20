from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.location_type import LocationType as LocationType_


__all__ = ["LocationType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class LocationType(LocationType_):
    """
    Location type

    This example value set defines a set of codes that can be used to
indicate the physical form of the Location.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/location-physical-type
    """

    class Meta:
        resource = _resource
