from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["GoalLifecycleStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class GoalLifecycleStatus:
    """
    GoalLifecycleStatus

    Codes that reflect the current state of a goal and whether the goal is
still being targeted.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/goal-status
    """

    proposed = CodeSystemConcept(
        {
            "code": "proposed",
            "definition": "A goal is proposed for this patient.",
            "display": "Proposed",
        }
    )
    """
    Proposed

    A goal is proposed for this patient.
    """

    planned = CodeSystemConcept(
        {
            "code": "planned",
            "definition": "A goal is planned for this patient.",
            "display": "Planned",
        }
    )
    """
    Planned

    A goal is planned for this patient.
    """

    accepted = CodeSystemConcept(
        {
            "code": "accepted",
            "concept": [
                {
                    "code": "active",
                    "definition": "The goal is being sought actively.",
                    "display": "Active",
                },
                {
                    "code": "on-hold",
                    "definition": "The goal remains a long term objective but is no longer being actively pursued for a temporary period of time.",
                    "display": "On Hold",
                },
                {
                    "code": "completed",
                    "definition": "The goal is no longer being sought.",
                    "display": "Completed",
                },
            ],
            "definition": "A proposed goal was accepted or acknowledged.",
            "display": "Accepted",
        }
    )
    """
    Accepted

    A proposed goal was accepted or acknowledged.
    """

    cancelled = CodeSystemConcept(
        {
            "code": "cancelled",
            "definition": "The goal has been abandoned.",
            "display": "Cancelled",
        }
    )
    """
    Cancelled

    The goal has been abandoned.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The goal was entered in error and voided.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The goal was entered in error and voided.
    """

    rejected = CodeSystemConcept(
        {
            "code": "rejected",
            "definition": "A proposed goal was rejected.",
            "display": "Rejected",
        }
    )
    """
    Rejected

    A proposed goal was rejected.
    """

    class Meta:
        resource = _resource
