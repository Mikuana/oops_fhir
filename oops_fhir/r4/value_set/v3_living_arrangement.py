from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_living_arrangement import (
    v3LivingArrangement as v3LivingArrangement_,
)


__all__ = ["v3LivingArrangement"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3LivingArrangement(v3LivingArrangement_):
    """
    v3 Code System LivingArrangement

     A code depicting the living arrangements of a person

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-LivingArrangement
    """

    class Meta:
        resource = _resource
