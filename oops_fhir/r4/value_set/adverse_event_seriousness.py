from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.adverse_event_seriousness import (
    AdverseEventSeriousness as AdverseEventSeriousness_,
)


__all__ = ["AdverseEventSeriousness"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AdverseEventSeriousness(AdverseEventSeriousness_):
    """
    AdverseEventSeriousness

    Overall seriousness of this event for the patient.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/adverse-event-seriousness
    """

    class Meta:
        resource = _resource
