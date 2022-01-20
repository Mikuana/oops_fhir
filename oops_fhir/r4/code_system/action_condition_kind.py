from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ActionConditionKind"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ActionConditionKind:
    """
    ActionConditionKind

    Defines the kinds of conditions that can appear on actions.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/action-condition-kind
    """

    applicability = CodeSystemConcept(
        {
            "code": "applicability",
            "definition": "The condition describes whether or not a given action is applicable.",
            "display": "Applicability",
        }
    )
    """
    Applicability

    The condition describes whether or not a given action is applicable.
    """

    start = CodeSystemConcept(
        {
            "code": "start",
            "definition": "The condition is a starting condition for the action.",
            "display": "Start",
        }
    )
    """
    Start

    The condition is a starting condition for the action.
    """

    stop = CodeSystemConcept(
        {
            "code": "stop",
            "definition": "The condition is a stop, or exit condition for the action.",
            "display": "Stop",
        }
    )
    """
    Stop

    The condition is a stop, or exit condition for the action.
    """

    class Meta:
        resource = _resource
