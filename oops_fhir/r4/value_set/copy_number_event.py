from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.copy_number_event import (
    CopyNumberEvent as CopyNumberEvent_,
)


__all__ = ["CopyNumberEvent"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CopyNumberEvent(CopyNumberEvent_):
    """
    CopyNumberEvent

    Copy Number Event.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/copy-number-event
    """

    class Meta:
        resource = _resource
