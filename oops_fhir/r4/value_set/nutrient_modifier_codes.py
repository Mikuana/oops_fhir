from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["NutrientModifierCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class NutrientModifierCodes(ValueSet):
    """
    Nutrient Modifier Codes

    NutrientModifier :  Codes for types of nutrients that are being modified
such as carbohydrate or sodium.  This value set includes codes from
[SNOMED CT](http://snomed.info/sct) where concept is-a 226355009
(Nutrients(substance)), and the concepts for Sodium, Potassium and
Fluid. This is provided as a suggestive example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/nutrient-code
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
