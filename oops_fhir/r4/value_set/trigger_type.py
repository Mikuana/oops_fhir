from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.trigger_type import TriggerType as TriggerType_


__all__ = ["TriggerType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TriggerType(TriggerType_):
    """
    TriggerType

    The type of trigger.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/trigger-type
    """

    class Meta:
        resource = _resource
