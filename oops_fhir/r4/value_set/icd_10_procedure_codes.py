from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.icd_10_procedure_codes import (
    ICD10ProcedureCodes as ICD10ProcedureCodes_,
)


__all__ = ["ICD10ProcedureCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ICD10ProcedureCodes(ICD10ProcedureCodes_):
    """
    ICD-10 Procedure Codes

    This value set includes sample ICD-10 Procedure codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/icd-10-procedures
    """

    class Meta:
        resource = _resource
