from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExceptionCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExceptionCodes:
    """
    Exception Codes

    This value set includes sample Exception codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/claim-exception
    """

    student = CodeSystemConcept(
        {
            "code": "student",
            "definition": "Fulltime Student",
            "display": "Student (Fulltime)",
        }
    )
    """
    Student (Fulltime)

    Fulltime Student
    """

    disabled = CodeSystemConcept(
        {"code": "disabled", "definition": "Disabled", "display": "Disabled"}
    )
    """
    Disabled

    Disabled
    """

    class Meta:
        resource = _resource
