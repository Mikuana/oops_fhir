from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.example_diagnosis_on_admission_codes import (
    ExampleDiagnosisOnAdmissionCodes as ExampleDiagnosisOnAdmissionCodes_,
)


__all__ = ["ExampleDiagnosisOnAdmissionCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExampleDiagnosisOnAdmissionCodes(ExampleDiagnosisOnAdmissionCodes_):
    """
    Example Diagnosis on Admission Codes

    This value set includes example Diagnosis on Admission codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/ex-diagnosis-on-admission
    """

    class Meta:
        resource = _resource
