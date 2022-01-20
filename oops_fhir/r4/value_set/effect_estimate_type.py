from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.effect_estimate_type import (
    EffectEstimateType as EffectEstimateType_,
)


__all__ = ["EffectEstimateType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EffectEstimateType(EffectEstimateType_):
    """
    EffectEstimateType

    Whether the effect estimate is an absolute effect estimate (absolute
difference) or a relative effect estimate (relative difference), and the
specific type of effect estimate (eg relative risk or median
difference).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/effect-estimate-type
    """

    class Meta:
        resource = _resource
