from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SearchEntryMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SearchEntryMode:
    """
    SearchEntryMode

    Why an entry is in the result set - whether it's included as a match or
because of an _include requirement, or to convey information or warning
information about the search process.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/search-entry-mode
    """

    match = CodeSystemConcept(
        {
            "code": "match",
            "definition": "This resource matched the search specification.",
            "display": "Match",
        }
    )
    """
    Match

    This resource matched the search specification.
    """

    include = CodeSystemConcept(
        {
            "code": "include",
            "definition": "This resource is returned because it is referred to from another resource in the search set.",
            "display": "Include",
        }
    )
    """
    Include

    This resource is returned because it is referred to from another resource in the search set.
    """

    outcome = CodeSystemConcept(
        {
            "code": "outcome",
            "definition": "An OperationOutcome that provides additional information about the processing of a search.",
            "display": "Outcome",
        }
    )
    """
    Outcome

    An OperationOutcome that provides additional information about the processing of a search.
    """

    class Meta:
        resource = _resource
