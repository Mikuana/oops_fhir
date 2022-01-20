from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["FlagPriorityCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class FlagPriorityCodes:
    """
    Flag Priority Codes

    This value set is provided as an exemplar. The value set is driven by
IHE Table B.8-4: Abnormal Flags, Alert Priority.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/flag-priority-code
    """

    pn = CodeSystemConcept(
        {"code": "PN", "definition": "No alarm.", "display": "No alarm"}
    )
    """
    No alarm

    No alarm.
    """

    pl = CodeSystemConcept(
        {"code": "PL", "definition": "Low priority.", "display": "Low priority"}
    )
    """
    Low priority

    Low priority.
    """

    pm = CodeSystemConcept(
        {"code": "PM", "definition": "Medium priority.", "display": "Medium priority"}
    )
    """
    Medium priority

    Medium priority.
    """

    ph = CodeSystemConcept(
        {"code": "PH", "definition": "High priority.", "display": "High priority"}
    )
    """
    High priority

    High priority.
    """

    class Meta:
        resource = _resource
