from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["EncounterReasonCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EncounterReasonCodes(ValueSet):
    """
    Encounter Reason Codes

    This examples value set defines the set of codes that can be used to
indicate reasons for an encounter.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/encounter-reason
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
