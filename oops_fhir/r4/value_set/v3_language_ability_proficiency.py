from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_language_ability_proficiency import (
    v3LanguageAbilityProficiency as v3LanguageAbilityProficiency_,
)


__all__ = ["v3LanguageAbilityProficiency"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3LanguageAbilityProficiency(v3LanguageAbilityProficiency_):
    """
    v3 Code System LanguageAbilityProficiency

     A value representing the level of proficiency in a language.  Example:
Excellent, good, fair, poor.  OpenIssue:  Description copied from
Concept Domain of same name.  Must be verified.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-LanguageAbilityProficiency
    """

    class Meta:
        resource = _resource
