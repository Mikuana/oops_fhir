from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ConditionDiagnosisSeverity"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConditionDiagnosisSeverity(ValueSet):
    """
    Condition/Diagnosis Severity

    Preferred value set for Condition/Diagnosis severity grading.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/condition-severity
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
