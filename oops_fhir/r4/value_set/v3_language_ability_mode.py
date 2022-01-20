from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_language_ability_mode import (
    v3LanguageAbilityMode as v3LanguageAbilityMode_,
)


__all__ = ["v3LanguageAbilityMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3LanguageAbilityMode(v3LanguageAbilityMode_):
    """
    v3 Code System LanguageAbilityMode

     A value representing the method of expression of the language.
Example:  Expressed spoken, expressed written, expressed signed,
received spoken, received written, received signed.  OpenIssue:
Description copied from Concept Domain of same name.  Must be verified.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-LanguageAbilityMode
    """

    class Meta:
        resource = _resource
