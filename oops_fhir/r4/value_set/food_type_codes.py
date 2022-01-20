from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["FoodTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FoodTypeCodes(SNOMEDCT):
    """
    Food Type Codes

    This value set represents codes for types of foods and is provided as a
suggestive example. It include codes from [SNOMED
CT](http://snomed.info/sct) where concept is-a 255620007 (Foods
(substance)).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/food-type
    """

    class Meta:
        resource = _resource
