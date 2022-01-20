from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_encounter_special_courtesy import (
    v3EncounterSpecialCourtesy as v3EncounterSpecialCourtesy_,
)


__all__ = ["v3EncounterSpecialCourtesy"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EncounterSpecialCourtesy(v3EncounterSpecialCourtesy_):
    """
    v3 Code System EncounterSpecialCourtesy

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-EncounterSpecialCourtesy
    """

    class Meta:
        resource = _resource
