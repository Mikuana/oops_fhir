from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExampleProgramReasonCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExampleProgramReasonCodes:
    """
    Example Program Reason Codes

    This value set includes sample Program Reason Span codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/ex-programcode
    """

    as_ = CodeSystemConcept(
        {"code": "as", "definition": "Child Asthma Program", "display": "Child Asthma"}
    )
    """
    Child Asthma

    Child Asthma Program
    """

    hd = CodeSystemConcept(
        {"code": "hd", "definition": "Hemodialysis Program.", "display": "Hemodialysis"}
    )
    """
    Hemodialysis

    Hemodialysis Program.
    """

    auscr = CodeSystemConcept(
        {
            "code": "auscr",
            "definition": "Autism Screening Program.",
            "display": "Autism Screening",
        }
    )
    """
    Autism Screening

    Autism Screening Program.
    """

    none = CodeSystemConcept(
        {"code": "none", "definition": "No program code applies.", "display": "None"}
    )
    """
    None

    No program code applies.
    """

    class Meta:
        resource = _resource
