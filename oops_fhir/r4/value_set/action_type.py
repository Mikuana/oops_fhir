from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.action_type import ActionType as ActionType_


__all__ = ["ActionType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ActionType(ActionType_):
    """
    ActionType

    The type of action to be performed.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/action-type
    """

    class Meta:
        resource = _resource
