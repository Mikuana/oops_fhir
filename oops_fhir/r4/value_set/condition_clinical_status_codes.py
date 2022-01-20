from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.condition_clinical_status_codes import (
    ConditionClinicalStatusCodes as ConditionClinicalStatusCodes_,
)


__all__ = ["ConditionClinicalStatusCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConditionClinicalStatusCodes(ConditionClinicalStatusCodes_):
    """
    Condition Clinical Status Codes

    Preferred value set for Condition Clinical Status.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/condition-clinical
    """

    class Meta:
        resource = _resource
