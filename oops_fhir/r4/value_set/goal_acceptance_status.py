from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.goal_acceptance_status import (
    GoalAcceptanceStatus as GoalAcceptanceStatus_,
)


__all__ = ["GoalAcceptanceStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class GoalAcceptanceStatus(GoalAcceptanceStatus_):
    """
    GoalAcceptanceStatus

    Codes indicating whether the goal has been accepted by a stakeholder.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/goal-acceptance-status
    """

    class Meta:
        resource = _resource
