from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.goal_status_reason import (
    GoalStatusReason as GoalStatusReason_,
)


__all__ = ["GoalStatusReason"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class GoalStatusReason(GoalStatusReason_):
    """
    Goal status reason

    Example codes indicating the reason for a current status.  Note that
these are in no way complete and might not even be appropriate for some
uses.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/goal-status-reason
    """

    class Meta:
        resource = _resource
