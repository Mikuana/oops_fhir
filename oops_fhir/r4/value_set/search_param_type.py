from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.search_param_type import (
    SearchParamType as SearchParamType_,
)


__all__ = ["SearchParamType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SearchParamType(SearchParamType_):
    """
    SearchParamType

    Data types allowed to be used for search parameters.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/search-param-type
    """

    class Meta:
        resource = _resource
