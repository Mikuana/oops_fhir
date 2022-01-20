from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.goal_achievement_status import (
    GoalAchievementStatus as GoalAchievementStatus_,
)


__all__ = ["GoalAchievementStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class GoalAchievementStatus(GoalAchievementStatus_):
    """
    Goal achievement status

    Describes the progression, or lack thereof, towards the goal against the
target.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/goal-achievement
    """

    class Meta:
        resource = _resource
