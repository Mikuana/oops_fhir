from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.action_condition_kind import (
    ActionConditionKind as ActionConditionKind_,
)


__all__ = ["ActionConditionKind"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ActionConditionKind(ActionConditionKind_):
    """
    ActionConditionKind

    Defines the kinds of conditions that can appear on actions.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/action-condition-kind
    """

    class Meta:
        resource = _resource
