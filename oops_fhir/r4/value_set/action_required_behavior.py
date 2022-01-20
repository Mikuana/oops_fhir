from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.action_required_behavior import (
    ActionRequiredBehavior as ActionRequiredBehavior_,
)


__all__ = ["ActionRequiredBehavior"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ActionRequiredBehavior(ActionRequiredBehavior_):
    """
    ActionRequiredBehavior

    Defines expectations around whether an action or action group is
required.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/action-required-behavior
    """

    class Meta:
        resource = _resource
