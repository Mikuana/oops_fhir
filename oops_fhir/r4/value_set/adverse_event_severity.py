from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.adverse_event_severity import (
    AdverseEventSeverity as AdverseEventSeverity_,
)


__all__ = ["AdverseEventSeverity"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AdverseEventSeverity(AdverseEventSeverity_):
    """
    AdverseEventSeverity

    The severity of the adverse event itself, in direct relation to the
subject.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/adverse-event-severity
    """

    class Meta:
        resource = _resource
