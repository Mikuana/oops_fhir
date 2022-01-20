from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.adverse_event_causality_assessment import (
    AdverseEventCausalityAssessment as AdverseEventCausalityAssessment_,
)


__all__ = ["AdverseEventCausalityAssessment"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AdverseEventCausalityAssessment(AdverseEventCausalityAssessment_):
    """
    AdverseEventCausalityAssessment

    Codes for the assessment of whether the entity caused the event.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/adverse-event-causality-assess
    """

    class Meta:
        resource = _resource
