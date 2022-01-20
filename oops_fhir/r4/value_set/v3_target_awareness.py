from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_target_awareness import (
    v3TargetAwareness as v3TargetAwareness_,
)


__all__ = ["v3TargetAwareness"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3TargetAwareness(v3TargetAwareness_):
    """
    v3 Code System TargetAwareness

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-TargetAwareness
    """

    class Meta:
        resource = _resource
