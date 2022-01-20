from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["GoalRelationshipType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class GoalRelationshipType:
    """
    GoalRelationshipType

    Types of relationships between two goals.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/goal-relationship-type
    """

    predecessor = CodeSystemConcept(
        {
            "code": "predecessor",
            "definition": "Indicates that the target goal is one which must be met before striving for the current goal.",
            "display": "Predecessor",
        }
    )
    """
    Predecessor

    Indicates that the target goal is one which must be met before striving for the current goal.
    """

    successor = CodeSystemConcept(
        {
            "code": "successor",
            "definition": "Indicates that the target goal is a desired objective once the current goal is met.",
            "display": "Successor",
        }
    )
    """
    Successor

    Indicates that the target goal is a desired objective once the current goal is met.
    """

    replacement = CodeSystemConcept(
        {
            "code": "replacement",
            "definition": "Indicates that this goal has been replaced by the target goal.",
            "display": "Replacement",
        }
    )
    """
    Replacement

    Indicates that this goal has been replaced by the target goal.
    """

    milestone = CodeSystemConcept(
        {
            "code": "milestone",
            "definition": 'Indicates that the target goal is considered to be a "piece" of attaining this goal.',
            "display": "Milestone",
        }
    )
    """
    Milestone

    Indicates that the target goal is considered to be a "piece" of attaining this goal.
    """

    other = CodeSystemConcept(
        {
            "code": "other",
            "definition": "Indicates that the relationship is not covered by one of the pre-defined codes.  (An extension may convey more information about the meaning of the relationship.).",
            "display": "Other",
        }
    )
    """
    Other

    Indicates that the relationship is not covered by one of the pre-defined codes.  (An extension may convey more information about the meaning of the relationship.).
    """

    class Meta:
        resource = _resource
