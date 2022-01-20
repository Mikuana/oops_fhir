from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.adverse_event_causality_method import (
    AdverseEventCausalityMethod as AdverseEventCausalityMethod_,
)


__all__ = ["AdverseEventCausalityMethod"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AdverseEventCausalityMethod(AdverseEventCausalityMethod_):
    """
    AdverseEventCausalityMethod

    TODO.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/adverse-event-causality-method
    """

    class Meta:
        resource = _resource
