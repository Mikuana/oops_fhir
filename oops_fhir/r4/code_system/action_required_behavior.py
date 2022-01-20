from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ActionRequiredBehavior"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ActionRequiredBehavior:
    """
    ActionRequiredBehavior

    Defines expectations around whether an action or action group is
required.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/action-required-behavior
    """

    must = CodeSystemConcept(
        {
            "code": "must",
            "definition": "An action with this behavior must be included in the actions processed by the end user; the end user SHALL NOT choose not to include this action.",
            "display": "Must",
        }
    )
    """
    Must

    An action with this behavior must be included in the actions processed by the end user; the end user SHALL NOT choose not to include this action.
    """

    could = CodeSystemConcept(
        {
            "code": "could",
            "definition": "An action with this behavior may be included in the set of actions processed by the end user.",
            "display": "Could",
        }
    )
    """
    Could

    An action with this behavior may be included in the set of actions processed by the end user.
    """

    must_unless_documented = CodeSystemConcept(
        {
            "code": "must-unless-documented",
            "definition": "An action with this behavior must be included in the set of actions processed by the end user, unless the end user provides documentation as to why the action was not included.",
            "display": "Must Unless Documented",
        }
    )
    """
    Must Unless Documented

    An action with this behavior must be included in the set of actions processed by the end user, unless the end user provides documentation as to why the action was not included.
    """

    class Meta:
        resource = _resource
