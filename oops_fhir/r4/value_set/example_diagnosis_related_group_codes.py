from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.example_diagnosis_related_group_codes import (
    ExampleDiagnosisRelatedGroupCodes as ExampleDiagnosisRelatedGroupCodes_,
)


__all__ = ["ExampleDiagnosisRelatedGroupCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExampleDiagnosisRelatedGroupCodes(ExampleDiagnosisRelatedGroupCodes_):
    """
    Example Diagnosis Related Group Codes

    This value set includes example Diagnosis Related Group codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/ex-diagnosisrelatedgroup
    """

    class Meta:
        resource = _resource
