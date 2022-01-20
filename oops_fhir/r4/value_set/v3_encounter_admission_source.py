from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_encounter_admission_source import (
    v3EncounterAdmissionSource as v3EncounterAdmissionSource_,
)


__all__ = ["v3EncounterAdmissionSource"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EncounterAdmissionSource(v3EncounterAdmissionSource_):
    """
    v3 Code System EncounterAdmissionSource

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-EncounterAdmissionSource
    """

    class Meta:
        resource = _resource
