from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.action_cardinality_behavior import (
    ActionCardinalityBehavior as ActionCardinalityBehavior_,
)


__all__ = ["ActionCardinalityBehavior"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ActionCardinalityBehavior(ActionCardinalityBehavior_):
    """
    ActionCardinalityBehavior

    Defines behavior for an action or a group for how many times that item
may be repeated.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/action-cardinality-behavior
    """

    class Meta:
        resource = _resource
