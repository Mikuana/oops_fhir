from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["AllergyIntoleranceSubstanceProductConditionAndNegationCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AllergyIntoleranceSubstanceProductConditionAndNegationCodes(ValueSet):
    """
    AllergyIntolerance Substance/Product, Condition and Negation Codes

    This value set includes concept codes for specific
substances/pharmaceutical products, allergy or intolerance conditions,
and negation/exclusion codes to specify the absence of specific types of
allergies or intolerances.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/allergyintolerance-code
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
