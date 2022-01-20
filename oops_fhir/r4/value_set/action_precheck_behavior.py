from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.action_precheck_behavior import (
    ActionPrecheckBehavior as ActionPrecheckBehavior_,
)


__all__ = ["ActionPrecheckBehavior"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ActionPrecheckBehavior(ActionPrecheckBehavior_):
    """
    ActionPrecheckBehavior

    Defines selection frequency behavior for an action or group.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/action-precheck-behavior
    """

    class Meta:
        resource = _resource
