from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["StructureDefinitionKind"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class StructureDefinitionKind:
    """
    StructureDefinitionKind

    Defines the type of structure that a definition is describing.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/structure-definition-kind
    """

    primitive_type = CodeSystemConcept(
        {
            "code": "primitive-type",
            "definition": "A primitive type that has a value and an extension. These can be used throughout complex datatype, Resource and extension definitions. Only the base specification can define primitive types.",
            "display": "Primitive Data Type",
        }
    )
    """
    Primitive Data Type

    A primitive type that has a value and an extension. These can be used throughout complex datatype, Resource and extension definitions. Only the base specification can define primitive types.
    """

    complex_type = CodeSystemConcept(
        {
            "code": "complex-type",
            "definition": "A  complex structure that defines a set of data elements that is suitable for use in 'resources'. The base specification defines a number of complex types, and other specifications can define additional types. These factory do not have a maintained identity.",
            "display": "Complex Data Type",
        }
    )
    """
    Complex Data Type

    A  complex structure that defines a set of data elements that is suitable for use in 'resources'. The base specification defines a number of complex types, and other specifications can define additional types. These factory do not have a maintained identity.
    """

    resource = CodeSystemConcept(
        {
            "code": "resource",
            "definition": "A 'resource' - a directed acyclic graph of elements that aggregrates other types into an identifiable entity. The base FHIR resources are defined by the FHIR specification itself but other 'resources' can be defined in additional specifications (though these will not be recognised as 'resources' by the FHIR specification (i.e. they do not get end-points etc, or act as the targets of references in FHIR defined resources - though other specificatiosn can treat them this way).",
            "display": "Resource",
        }
    )
    """
    Resource

    A 'resource' - a directed acyclic graph of elements that aggregrates other types into an identifiable entity. The base FHIR resources are defined by the FHIR specification itself but other 'resources' can be defined in additional specifications (though these will not be recognised as 'resources' by the FHIR specification (i.e. they do not get end-points etc, or act as the targets of references in FHIR defined resources - though other specificatiosn can treat them this way).
    """

    logical = CodeSystemConcept(
        {
            "code": "logical",
            "definition": "A pattern or a template that is not intended to be a real resource or complex type.",
            "display": "Logical",
        }
    )
    """
    Logical

    A pattern or a template that is not intended to be a real resource or complex type.
    """

    class Meta:
        resource = _resource
