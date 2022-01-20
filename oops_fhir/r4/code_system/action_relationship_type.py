from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ActionRelationshipType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ActionRelationshipType:
    """
    ActionRelationshipType

    Defines the types of relationships between actions.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/action-relationship-type
    """

    before_start = CodeSystemConcept(
        {
            "code": "before-start",
            "definition": "The action must be performed before the start of the related action.",
            "display": "Before Start",
        }
    )
    """
    Before Start

    The action must be performed before the start of the related action.
    """

    before = CodeSystemConcept(
        {
            "code": "before",
            "definition": "The action must be performed before the related action.",
            "display": "Before",
        }
    )
    """
    Before

    The action must be performed before the related action.
    """

    before_end = CodeSystemConcept(
        {
            "code": "before-end",
            "definition": "The action must be performed before the end of the related action.",
            "display": "Before End",
        }
    )
    """
    Before End

    The action must be performed before the end of the related action.
    """

    concurrent_with_start = CodeSystemConcept(
        {
            "code": "concurrent-with-start",
            "definition": "The action must be performed concurrent with the start of the related action.",
            "display": "Concurrent With Start",
        }
    )
    """
    Concurrent With Start

    The action must be performed concurrent with the start of the related action.
    """

    concurrent = CodeSystemConcept(
        {
            "code": "concurrent",
            "definition": "The action must be performed concurrent with the related action.",
            "display": "Concurrent",
        }
    )
    """
    Concurrent

    The action must be performed concurrent with the related action.
    """

    concurrent_with_end = CodeSystemConcept(
        {
            "code": "concurrent-with-end",
            "definition": "The action must be performed concurrent with the end of the related action.",
            "display": "Concurrent With End",
        }
    )
    """
    Concurrent With End

    The action must be performed concurrent with the end of the related action.
    """

    after_start = CodeSystemConcept(
        {
            "code": "after-start",
            "definition": "The action must be performed after the start of the related action.",
            "display": "After Start",
        }
    )
    """
    After Start

    The action must be performed after the start of the related action.
    """

    after = CodeSystemConcept(
        {
            "code": "after",
            "definition": "The action must be performed after the related action.",
            "display": "After",
        }
    )
    """
    After

    The action must be performed after the related action.
    """

    after_end = CodeSystemConcept(
        {
            "code": "after-end",
            "definition": "The action must be performed after the end of the related action.",
            "display": "After End",
        }
    )
    """
    After End

    The action must be performed after the end of the related action.
    """

    class Meta:
        resource = _resource
