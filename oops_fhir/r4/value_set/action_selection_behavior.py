from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.action_selection_behavior import (
    ActionSelectionBehavior as ActionSelectionBehavior_,
)


__all__ = ["ActionSelectionBehavior"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ActionSelectionBehavior(ActionSelectionBehavior_):
    """
    ActionSelectionBehavior

    Defines selection behavior of a group.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/action-selection-behavior
    """

    class Meta:
        resource = _resource
