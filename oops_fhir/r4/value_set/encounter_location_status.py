from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.encounter_location_status import (
    EncounterLocationStatus as EncounterLocationStatus_,
)


__all__ = ["EncounterLocationStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EncounterLocationStatus(EncounterLocationStatus_):
    """
    EncounterLocationStatus

    The status of the location.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/encounter-location-status
    """

    class Meta:
        resource = _resource
