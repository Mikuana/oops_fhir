from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ActionSelectionBehavior"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ActionSelectionBehavior:
    """
    ActionSelectionBehavior

    Defines selection behavior of a group.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/action-selection-behavior
    """

    any_ = CodeSystemConcept(
        {
            "code": "any",
            "definition": "Any number of the actions in the group may be chosen, from zero to all.",
            "display": "Any",
        }
    )
    """
    Any

    Any number of the actions in the group may be chosen, from zero to all.
    """

    all_ = CodeSystemConcept(
        {
            "code": "all",
            "definition": "All the actions in the group must be selected as a single unit.",
            "display": "All",
        }
    )
    """
    All

    All the actions in the group must be selected as a single unit.
    """

    all_or_none = CodeSystemConcept(
        {
            "code": "all-or-none",
            "definition": "All the actions in the group are meant to be chosen as a single unit: either all must be selected by the end user, or none may be selected.",
            "display": "All Or None",
        }
    )
    """
    All Or None

    All the actions in the group are meant to be chosen as a single unit: either all must be selected by the end user, or none may be selected.
    """

    exactly_one = CodeSystemConcept(
        {
            "code": "exactly-one",
            "definition": "The end user must choose one and only one of the selectable actions in the group. The user SHALL NOT choose none of the actions in the group.",
            "display": "Exactly One",
        }
    )
    """
    Exactly One

    The end user must choose one and only one of the selectable actions in the group. The user SHALL NOT choose none of the actions in the group.
    """

    at_most_one = CodeSystemConcept(
        {
            "code": "at-most-one",
            "definition": "The end user may choose zero or at most one of the actions in the group.",
            "display": "At Most One",
        }
    )
    """
    At Most One

    The end user may choose zero or at most one of the actions in the group.
    """

    one_or_more = CodeSystemConcept(
        {
            "code": "one-or-more",
            "definition": "The end user must choose a minimum of one, and as many additional as desired.",
            "display": "One Or More",
        }
    )
    """
    One Or More

    The end user must choose a minimum of one, and as many additional as desired.
    """

    class Meta:
        resource = _resource
