from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.goal_category import GoalCategory as GoalCategory_


__all__ = ["GoalCategory"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class GoalCategory(GoalCategory_):
    """
    Goal category

    Example codes for grouping goals to use for filtering or presentation.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/goal-category
    """

    class Meta:
        resource = _resource
