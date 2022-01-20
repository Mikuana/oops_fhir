from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.search_entry_mode import (
    SearchEntryMode as SearchEntryMode_,
)


__all__ = ["SearchEntryMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SearchEntryMode(SearchEntryMode_):
    """
    SearchEntryMode

    Why an entry is in the result set - whether it's included as a match or
because of an _include requirement, or to convey information or warning
information about the search process.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/search-entry-mode
    """

    class Meta:
        resource = _resource
