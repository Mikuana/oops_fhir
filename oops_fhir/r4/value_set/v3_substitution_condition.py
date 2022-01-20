from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_substitution_condition import (
    v3SubstitutionCondition as v3SubstitutionCondition_,
)


__all__ = ["v3SubstitutionCondition"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3SubstitutionCondition(v3SubstitutionCondition_):
    """
    v3 Code System SubstitutionCondition

     Identifies what sort of change is permitted or has occurred between the
item that was ordered/requested and the one that was/will be provided.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-SubstitutionCondition
    """

    class Meta:
        resource = _resource
