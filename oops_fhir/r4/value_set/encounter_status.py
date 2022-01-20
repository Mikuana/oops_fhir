from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.encounter_status import (
    EncounterStatus as EncounterStatus_,
)


__all__ = ["EncounterStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EncounterStatus(EncounterStatus_):
    """
    EncounterStatus

    Current state of the encounter.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/encounter-status
    """

    class Meta:
        resource = _resource
