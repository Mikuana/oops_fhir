from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SortDirection"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SortDirection:
    """
    SortDirection

    The possible sort directions, ascending or descending.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/sort-direction
    """

    ascending = CodeSystemConcept(
        {
            "code": "ascending",
            "definition": "Sort by the value ascending, so that lower values appear first.",
            "display": "Ascending",
        }
    )
    """
    Ascending

    Sort by the value ascending, so that lower values appear first.
    """

    descending = CodeSystemConcept(
        {
            "code": "descending",
            "definition": "Sort by the value descending, so that lower values appear last.",
            "display": "Descending",
        }
    )
    """
    Descending

    Sort by the value descending, so that lower values appear last.
    """

    class Meta:
        resource = _resource
