from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.slot_status import SlotStatus as SlotStatus_


__all__ = ["SlotStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SlotStatus(SlotStatus_):
    """
    SlotStatus

    The free/busy status of the slot.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/slotstatus
    """

    class Meta:
        resource = _resource
