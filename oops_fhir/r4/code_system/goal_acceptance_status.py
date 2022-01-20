from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["GoalAcceptanceStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class GoalAcceptanceStatus:
    """
    GoalAcceptanceStatus

    Codes indicating whether the goal has been accepted by a stakeholder.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/goal-acceptance-status
    """

    agree = CodeSystemConcept(
        {
            "code": "agree",
            "definition": "Stakeholder supports pursuit of the goal.",
            "display": "Agree",
        }
    )
    """
    Agree

    Stakeholder supports pursuit of the goal.
    """

    disagree = CodeSystemConcept(
        {
            "code": "disagree",
            "definition": "Stakeholder is not in support of the pursuit of the goal.",
            "display": "Disagree",
        }
    )
    """
    Disagree

    Stakeholder is not in support of the pursuit of the goal.
    """

    pending = CodeSystemConcept(
        {
            "code": "pending",
            "definition": "Stakeholder has not yet made a decision on whether they support the goal.",
            "display": "Pending",
        }
    )
    """
    Pending

    Stakeholder has not yet made a decision on whether they support the goal.
    """

    class Meta:
        resource = _resource
