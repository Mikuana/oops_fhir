from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ActionCardinalityBehavior"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ActionCardinalityBehavior:
    """
    ActionCardinalityBehavior

    Defines behavior for an action or a group for how many times that item
may be repeated.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/action-cardinality-behavior
    """

    single = CodeSystemConcept(
        {
            "code": "single",
            "definition": "The action may only be selected one time.",
            "display": "Single",
        }
    )
    """
    Single

    The action may only be selected one time.
    """

    multiple = CodeSystemConcept(
        {
            "code": "multiple",
            "definition": "The action may be selected multiple times.",
            "display": "Multiple",
        }
    )
    """
    Multiple

    The action may be selected multiple times.
    """

    class Meta:
        resource = _resource
