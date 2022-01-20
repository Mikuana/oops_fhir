from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ConditionState"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ConditionState:
    """
    ConditionState

    Enumeration indicating whether the condition is currently active,
inactive, or has been resolved.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/condition-state
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "The condition is active.",
            "display": "Active",
        }
    )
    """
    Active

    The condition is active.
    """

    inactive = CodeSystemConcept(
        {
            "code": "inactive",
            "definition": "The condition is inactive, but not resolved.",
            "display": "Inactive",
        }
    )
    """
    Inactive

    The condition is inactive, but not resolved.
    """

    resolved = CodeSystemConcept(
        {
            "code": "resolved",
            "definition": "The condition is resolved.",
            "display": "Resolved",
        }
    )
    """
    Resolved

    The condition is resolved.
    """

    class Meta:
        resource = _resource
