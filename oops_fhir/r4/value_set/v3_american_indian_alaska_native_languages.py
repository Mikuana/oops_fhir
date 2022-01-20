from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_american_indian_alaska_native_languages import (
    v3AmericanIndianAlaskaNativeLanguages as v3AmericanIndianAlaskaNativeLanguages_,
)


__all__ = ["v3AmericanIndianAlaskaNativeLanguages"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3AmericanIndianAlaskaNativeLanguages(v3AmericanIndianAlaskaNativeLanguages_):
    """
    v3 Code System AmericanIndianAlaskaNativeLanguages

     American Indian and Alaska Native languages currently being used in the
United States.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-AmericanIndianAlaskaNativeLanguages
    """

    class Meta:
        resource = _resource
