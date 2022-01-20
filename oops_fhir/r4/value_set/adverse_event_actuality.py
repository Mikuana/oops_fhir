from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.adverse_event_actuality import (
    AdverseEventActuality as AdverseEventActuality_,
)


__all__ = ["AdverseEventActuality"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AdverseEventActuality(AdverseEventActuality_):
    """
    AdverseEventActuality

    Overall nature of the adverse event, e.g. real or potential.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/adverse-event-actuality
    """

    class Meta:
        resource = _resource
