from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.action_grouping_behavior import (
    ActionGroupingBehavior as ActionGroupingBehavior_,
)


__all__ = ["ActionGroupingBehavior"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ActionGroupingBehavior(ActionGroupingBehavior_):
    """
    ActionGroupingBehavior

    Defines organization behavior of a group.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/action-grouping-behavior
    """

    class Meta:
        resource = _resource
