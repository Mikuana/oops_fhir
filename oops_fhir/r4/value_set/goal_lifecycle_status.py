from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.goal_lifecycle_status import (
    GoalLifecycleStatus as GoalLifecycleStatus_,
)


__all__ = ["GoalLifecycleStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class GoalLifecycleStatus(GoalLifecycleStatus_):
    """
    GoalLifecycleStatus

    Codes that reflect the current state of a goal and whether the goal is
still being targeted.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/goal-status
    """

    class Meta:
        resource = _resource
