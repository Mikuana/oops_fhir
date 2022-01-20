from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.condition_state import ConditionState as ConditionState_


__all__ = ["ConditionState"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConditionState(ConditionState_):
    """
    ConditionState

    Enumeration indicating whether the condition is currently active,
inactive, or has been resolved.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/condition-state
    """

    class Meta:
        resource = _resource
