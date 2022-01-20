from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.search_comparator import (
    SearchComparator as SearchComparator_,
)


__all__ = ["SearchComparator"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SearchComparator(SearchComparator_):
    """
    SearchComparator

    What Search Comparator Codes are supported in search.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/search-comparator
    """

    class Meta:
        resource = _resource
