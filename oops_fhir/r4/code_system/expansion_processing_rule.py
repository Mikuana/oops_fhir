from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExpansionProcessingRule"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExpansionProcessingRule:
    """
    ExpansionProcessingRule

    Defines how concepts are processed into the expansion when it's for UI
presentation.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/expansion-processing-rule
    """

    all_codes = CodeSystemConcept(
        {
            "code": "all-codes",
            "definition": "The expansion (when in UI mode) includes all codes *and* any defined groups (in extensions).",
            "display": "All Codes",
        }
    )
    """
    All Codes

    The expansion (when in UI mode) includes all codes *and* any defined groups (in extensions).
    """

    ungrouped = CodeSystemConcept(
        {
            "code": "ungrouped",
            "definition": "The expanion (when in UI mode) lists the groups, and then any codes that have not been included in a group.",
            "display": "Groups + Ungrouped codes",
        }
    )
    """
    Groups + Ungrouped codes

    The expanion (when in UI mode) lists the groups, and then any codes that have not been included in a group.
    """

    groups_only = CodeSystemConcept(
        {
            "code": "groups-only",
            "definition": "The expansion (when in UI mode) only includes the defined groups.",
            "display": "Groups Only",
        }
    )
    """
    Groups Only

    The expansion (when in UI mode) only includes the defined groups.
    """

    class Meta:
        resource = _resource
