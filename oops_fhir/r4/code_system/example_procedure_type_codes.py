from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExampleProcedureTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExampleProcedureTypeCodes:
    """
    Example Procedure Type Codes

    This value set includes example Procedure Type codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/ex-procedure-type
    """

    primary = CodeSystemConcept(
        {
            "code": "primary",
            "definition": "The first procedure in a series required to produce and overall patient outcome.",
            "display": "Primary procedure",
        }
    )
    """
    Primary procedure

    The first procedure in a series required to produce and overall patient outcome.
    """

    secondary = CodeSystemConcept(
        {
            "code": "secondary",
            "definition": "The second procedure in a series required to produce and overall patient outcome.",
            "display": "Secondary procedure",
        }
    )
    """
    Secondary procedure

    The second procedure in a series required to produce and overall patient outcome.
    """

    class Meta:
        resource = _resource
