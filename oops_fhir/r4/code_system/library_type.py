from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["LibraryType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class LibraryType:
    """
    LibraryType

    The type of knowledge asset this library contains.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/library-type
    """

    logic_library = CodeSystemConcept(
        {
            "code": "logic-library",
            "definition": "The resource is a shareable library of formalized knowledge.",
            "display": "Logic Library",
        }
    )
    """
    Logic Library

    The resource is a shareable library of formalized knowledge.
    """

    model_definition = CodeSystemConcept(
        {
            "code": "model-definition",
            "definition": "The resource is a definition of an information model.",
            "display": "Model Definition",
        }
    )
    """
    Model Definition

    The resource is a definition of an information model.
    """

    asset_collection = CodeSystemConcept(
        {
            "code": "asset-collection",
            "definition": "The resource is a collection of knowledge assets.",
            "display": "Asset Collection",
        }
    )
    """
    Asset Collection

    The resource is a collection of knowledge assets.
    """

    module_definition = CodeSystemConcept(
        {
            "code": "module-definition",
            "definition": "The resource defines the dependencies, parameters, and data requirements for a particular module or evaluation context.",
            "display": "Module Definition",
        }
    )
    """
    Module Definition

    The resource defines the dependencies, parameters, and data requirements for a particular module or evaluation context.
    """

    class Meta:
        resource = _resource
