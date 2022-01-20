from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.adverse_event_outcome import (
    AdverseEventOutcome as AdverseEventOutcome_,
)


__all__ = ["AdverseEventOutcome"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AdverseEventOutcome(AdverseEventOutcome_):
    """
    AdverseEventOutcome

    TODO (and should this be required?).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/adverse-event-outcome
    """

    class Meta:
        resource = _resource
