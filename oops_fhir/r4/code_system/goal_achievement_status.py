from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["GoalAchievementStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class GoalAchievementStatus:
    """
    Goal achievement status

    Describes the progression, or lack thereof, towards the goal against the
target.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/goal-achievement
    """

    in_progress = CodeSystemConcept(
        {
            "code": "in-progress",
            "concept": [
                {
                    "code": "improving",
                    "definition": "The goal is being sought, and is progressing.",
                    "display": "Improving",
                },
                {
                    "code": "worsening",
                    "definition": "The goal is being sought, but is regressing.",
                    "display": "Worsening",
                },
                {
                    "code": "no-change",
                    "definition": "The goal is being sought, but the trend is flat.",
                    "display": "No Change",
                },
            ],
            "definition": "The goal is being sought but has not yet been reached. (Also applies if the goal was reached in the past but there has been regression and the goal is again being sought).",
            "display": "In Progress",
        }
    )
    """
    In Progress

    The goal is being sought but has not yet been reached. (Also applies if the goal was reached in the past but there has been regression and the goal is again being sought).
    """

    achieved = CodeSystemConcept(
        {
            "code": "achieved",
            "concept": [
                {
                    "code": "sustaining",
                    "definition": "The goal has been met, but ongoing activity is needed to sustain the goal objective.",
                    "display": "Sustaining",
                }
            ],
            "definition": "The goal has been met.",
            "display": "Achieved",
        }
    )
    """
    Achieved

    The goal has been met.
    """

    not_achieved = CodeSystemConcept(
        {
            "code": "not-achieved",
            "concept": [
                {
                    "code": "no-progress",
                    "definition": "The goal has not been met and little to no progress towards target.",
                    "display": "No Progress",
                },
                {
                    "code": "not-attainable",
                    "definition": "The goal is not possible to be met.",
                    "display": "Not Attainable",
                },
            ],
            "definition": "The goal has not been met and there might or might not have been progress towards target.",
            "display": "Not Achieved",
        }
    )
    """
    Not Achieved

    The goal has not been met and there might or might not have been progress towards target.
    """

    class Meta:
        resource = _resource
