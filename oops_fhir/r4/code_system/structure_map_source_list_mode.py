from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["StructureMapSourceListMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class StructureMapSourceListMode:
    """
    StructureMapSourceListMode

    If field is a list, how to manage the source.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/map-source-list-mode
    """

    first = CodeSystemConcept(
        {
            "code": "first",
            "definition": "Only process this rule for the first in the list.",
            "display": "First",
        }
    )
    """
    First

    Only process this rule for the first in the list.
    """

    not_first = CodeSystemConcept(
        {
            "code": "not_first",
            "definition": "Process this rule for all but the first.",
            "display": "All but the first",
        }
    )
    """
    All but the first

    Process this rule for all but the first.
    """

    last = CodeSystemConcept(
        {
            "code": "last",
            "definition": "Only process this rule for the last in the list.",
            "display": "Last",
        }
    )
    """
    Last

    Only process this rule for the last in the list.
    """

    not_last = CodeSystemConcept(
        {
            "code": "not_last",
            "definition": "Process this rule for all but the last.",
            "display": "All but the last",
        }
    )
    """
    All but the last

    Process this rule for all but the last.
    """

    only_one = CodeSystemConcept(
        {
            "code": "only_one",
            "definition": "Only process this rule is there is only item.",
            "display": "Enforce only one",
        }
    )
    """
    Enforce only one

    Only process this rule is there is only item.
    """

    class Meta:
        resource = _resource
