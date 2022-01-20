from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ICD10ProcedureCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ICD10ProcedureCodes:
    """
    ICD-10 Procedure Codes

    This value set includes sample ICD-10 Procedure codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://hl7.org/fhir/sid/ex-icd-10-procedures
    """

    one23001 = CodeSystemConcept(
        {"code": "123001", "definition": "Procedure 1", "display": "PROC-1"}
    )
    """
    PROC-1

    Procedure 1
    """

    one23002 = CodeSystemConcept(
        {"code": "123002", "definition": "Procedure 2", "display": "PROC-2"}
    )
    """
    PROC-2

    Procedure 2
    """

    one23003 = CodeSystemConcept(
        {"code": "123003", "definition": "Procedure 3", "display": "PROC-3"}
    )
    """
    PROC-3

    Procedure 3
    """

    class Meta:
        resource = _resource
