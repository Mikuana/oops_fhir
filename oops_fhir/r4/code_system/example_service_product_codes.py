from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExampleServiceProductCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExampleServiceProductCodes:
    """
    Example Service/Product Codes

    This value set includes a smattering of Service/Product codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://hl7.org/fhir/ex-serviceproduct
    """

    exam = CodeSystemConcept({"code": "exam", "definition": "Exam", "display": "Exam"})
    """
    Exam

    Exam
    """

    flushot = CodeSystemConcept(
        {"code": "flushot", "definition": "Flu shot", "display": "Flu shot"}
    )
    """
    Flu shot

    Flu shot
    """

    class Meta:
        resource = _resource
