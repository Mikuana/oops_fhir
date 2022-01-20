from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.example_diagnosis_type_codes import (
    ExampleDiagnosisTypeCodes as ExampleDiagnosisTypeCodes_,
)


__all__ = ["ExampleDiagnosisTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExampleDiagnosisTypeCodes(ExampleDiagnosisTypeCodes_):
    """
    Example Diagnosis Type Codes

    This value set includes example Diagnosis Type codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/ex-diagnosistype
    """

    class Meta:
        resource = _resource
