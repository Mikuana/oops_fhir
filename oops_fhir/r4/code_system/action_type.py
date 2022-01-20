from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ActionType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ActionType:
    """
    ActionType

    The type of action to be performed.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/action-type
    """

    create = CodeSystemConcept(
        {
            "code": "create",
            "definition": "The action is to create a new resource.",
            "display": "Create",
        }
    )
    """
    Create

    The action is to create a new resource.
    """

    update = CodeSystemConcept(
        {
            "code": "update",
            "definition": "The action is to update an existing resource.",
            "display": "Update",
        }
    )
    """
    Update

    The action is to update an existing resource.
    """

    remove = CodeSystemConcept(
        {
            "code": "remove",
            "definition": "The action is to remove an existing resource.",
            "display": "Remove",
        }
    )
    """
    Remove

    The action is to remove an existing resource.
    """

    fire_event = CodeSystemConcept(
        {
            "code": "fire-event",
            "definition": "The action is to fire a specific event.",
            "display": "Fire Event",
        }
    )
    """
    Fire Event

    The action is to fire a specific event.
    """

    class Meta:
        resource = _resource
