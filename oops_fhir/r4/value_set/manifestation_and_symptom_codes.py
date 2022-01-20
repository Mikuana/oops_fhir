from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["ManifestationAndSymptomCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ManifestationAndSymptomCodes(SNOMEDCT):
    """
    Manifestation and Symptom Codes

    Example value set for Manifestation and Symptom codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/manifestation-or-symptom
    """

    class Meta:
        resource = _resource
