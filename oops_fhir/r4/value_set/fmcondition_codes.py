from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.fmcondition_codes import (
    FMConditionCodes as FMConditionCodes_,
)


__all__ = ["FMConditionCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FMConditionCodes(FMConditionCodes_):
    """
    FM Condition Codes

    This value set includes sample Conditions codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/fm-conditions
    """

    class Meta:
        resource = _resource
