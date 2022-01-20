from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.search_modifier_code import (
    SearchModifierCode as SearchModifierCode_,
)


__all__ = ["SearchModifierCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SearchModifierCode(SearchModifierCode_):
    """
    SearchModifierCode

    A supported modifier for a search parameter.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/search-modifier-code
    """

    class Meta:
        resource = _resource
