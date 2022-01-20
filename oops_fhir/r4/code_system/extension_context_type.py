from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExtensionContextType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExtensionContextType:
    """
    ExtensionContextType

    How an extension context is interpreted.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/extension-context-type
    """

    fhirpath = CodeSystemConcept(
        {
            "code": "fhirpath",
            "definition": "The context is all elements that match the FHIRPath query found in the expression.",
            "display": "FHIRPath",
        }
    )
    """
    FHIRPath

    The context is all elements that match the FHIRPath query found in the expression.
    """

    element = CodeSystemConcept(
        {
            "code": "element",
            "definition": "The context is any element that has an ElementDefinition.id that matches that found in the expression. This includes ElementDefinition Ids that have slicing identifiers. The full path for the element is [url]#[elementid]. If there is no #, the Element id is one defined in the base specification.",
            "display": "Element ID",
        }
    )
    """
    Element ID

    The context is any element that has an ElementDefinition.id that matches that found in the expression. This includes ElementDefinition Ids that have slicing identifiers. The full path for the element is [url]#[elementid]. If there is no #, the Element id is one defined in the base specification.
    """

    extension = CodeSystemConcept(
        {
            "code": "extension",
            "definition": "The context is a particular extension from a particular StructureDefinition, and the expression is just a uri that identifies the extension.",
            "display": "Extension URL",
        }
    )
    """
    Extension URL

    The context is a particular extension from a particular StructureDefinition, and the expression is just a uri that identifies the extension.
    """

    class Meta:
        resource = _resource
