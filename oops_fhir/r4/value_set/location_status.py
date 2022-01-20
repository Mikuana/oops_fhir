from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.location_status import LocationStatus as LocationStatus_


__all__ = ["LocationStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class LocationStatus(LocationStatus_):
    """
    LocationStatus

    Indicates whether the location is still in use.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/location-status
    """

    class Meta:
        resource = _resource
