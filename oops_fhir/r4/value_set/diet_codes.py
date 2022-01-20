from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["DietCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DietCodes(SNOMEDCT):
    """
    Diet Codes

    Codes that can be used to indicate the type of food being ordered for a
patient. This value set is provided as a suggestive example. It includes
codes from [SNOMED CT](http://snomed.info/sct) where concept is-a
182922004 (Dietary regime (regime/therapy))

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/diet-type
    """

    class Meta:
        resource = _resource
