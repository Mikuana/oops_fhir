from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["GoalPriority"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class GoalPriority:
    """
    Goal priority

    Indicates the level of importance associated with reaching or sustaining
a goal.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/goal-priority
    """

    high_priority = CodeSystemConcept(
        {
            "code": "high-priority",
            "definition": "Indicates that the goal is of considerable importance and should be a primary focus of care delivery.",
            "display": "High Priority",
        }
    )
    """
    High Priority

    Indicates that the goal is of considerable importance and should be a primary focus of care delivery.
    """

    medium_priority = CodeSystemConcept(
        {
            "code": "medium-priority",
            "definition": "Indicates that the goal has a reasonable degree of importance and that concrete action should be taken towards the goal.  Attainment is not as critical as high-priority goals.",
            "display": "Medium Priority",
        }
    )
    """
    Medium Priority

    Indicates that the goal has a reasonable degree of importance and that concrete action should be taken towards the goal.  Attainment is not as critical as high-priority goals.
    """

    low_priority = CodeSystemConcept(
        {
            "code": "low-priority",
            "definition": "The goal is desirable but is not sufficiently important to devote significant resources to.  Achievement of the goal may be sought when incidental to achieving other goals.",
            "display": "Low Priority",
        }
    )
    """
    Low Priority

    The goal is desirable but is not sufficiently important to devote significant resources to.  Achievement of the goal may be sought when incidental to achieving other goals.
    """

    class Meta:
        resource = _resource
