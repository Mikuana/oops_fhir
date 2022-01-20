from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["StructureMapContextType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class StructureMapContextType:
    """
    StructureMapContextType

    How to interpret the context.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/map-context-type
    """

    type_ = CodeSystemConcept(
        {
            "code": "type",
            "definition": "The context specifies a type.",
            "display": "Type",
        }
    )
    """
    Type

    The context specifies a type.
    """

    variable = CodeSystemConcept(
        {
            "code": "variable",
            "definition": "The context specifies a variable.",
            "display": "Variable",
        }
    )
    """
    Variable

    The context specifies a variable.
    """

    class Meta:
        resource = _resource
