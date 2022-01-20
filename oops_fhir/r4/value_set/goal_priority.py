from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.goal_priority import GoalPriority as GoalPriority_


__all__ = ["GoalPriority"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class GoalPriority(GoalPriority_):
    """
    Goal priority

    Indicates the level of importance associated with reaching or sustaining
a goal.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/goal-priority
    """

    class Meta:
        resource = _resource
