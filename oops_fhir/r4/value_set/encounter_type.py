from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.encounter_type import EncounterType as EncounterType_


__all__ = ["EncounterType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EncounterType(EncounterType_):
    """
    Encounter type

    This example value set defines a set of codes that can be used to
indicate the type of encounter: a specific code indicating type of
service provided.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/encounter-type
    """

    class Meta:
        resource = _resource
