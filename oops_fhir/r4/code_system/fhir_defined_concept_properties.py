from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["FHIRDefinedConceptProperties"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class FHIRDefinedConceptProperties:
    """
    None

    A set of common concept properties for use on coded systems throughout
the FHIR eco-system.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/concept-properties
    """

    inactive = CodeSystemConcept(
        {
            "code": "inactive",
            "definition": "True if the concept is not considered active - e.g. not a valid concept any more. Property type is boolean, default value is false",
            "display": "Inactive",
        }
    )
    """
    Inactive

    True if the concept is not considered active - e.g. not a valid concept any more. Property type is boolean, default value is false
    """

    deprecated = CodeSystemConcept(
        {
            "code": "deprecated",
            "definition": "The date at which a concept was deprecated. Concepts that are deprecated but not inactive can still be used, but their use is discouraged, and they should be expected to be made inactive in a future release. Property type is dateTime",
            "display": "Deprecated",
        }
    )
    """
    Deprecated

    The date at which a concept was deprecated. Concepts that are deprecated but not inactive can still be used, but their use is discouraged, and they should be expected to be made inactive in a future release. Property type is dateTime
    """

    not_selectable = CodeSystemConcept(
        {
            "code": "notSelectable",
            "definition": "The concept is not intended to be chosen by the user - only intended to be used as a selector for other concepts. Note, though, that the interpretation of this is highly contextual; all concepts are selectable in some context. Property type is boolean",
            "display": "Not Selectable",
        }
    )
    """
    Not Selectable

    The concept is not intended to be chosen by the user - only intended to be used as a selector for other concepts. Note, though, that the interpretation of this is highly contextual; all concepts are selectable in some context. Property type is boolean
    """

    parent = CodeSystemConcept(
        {
            "code": "parent",
            "definition": "The concept identified in this property is a parent of the concept on which it is a property. The property type will be 'code'. The meaning of 'parent' is defined by the hierarchyMeaning attribute",
            "display": "Parent",
        }
    )
    """
    Parent

    The concept identified in this property is a parent of the concept on which it is a property. The property type will be 'code'. The meaning of 'parent' is defined by the hierarchyMeaning attribute
    """

    child = CodeSystemConcept(
        {
            "code": "child",
            "definition": "The concept identified in this property is a child of the concept on which it is a property. The property type will be 'code'. The meaning of 'child' is defined by the hierarchyMeaning attribute",
            "display": "Child",
        }
    )
    """
    Child

    The concept identified in this property is a child of the concept on which it is a property. The property type will be 'code'. The meaning of 'child' is defined by the hierarchyMeaning attribute
    """

    class Meta:
        resource = _resource
