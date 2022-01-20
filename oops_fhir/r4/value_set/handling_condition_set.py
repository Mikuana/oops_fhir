from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.handling_condition_set import (
    HandlingConditionSet as HandlingConditionSet_,
)


__all__ = ["HandlingConditionSet"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class HandlingConditionSet(HandlingConditionSet_):
    """
    HandlingConditionSet

    Set of handling instructions prior testing of the specimen.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/handling-condition
    """

    class Meta:
        resource = _resource
