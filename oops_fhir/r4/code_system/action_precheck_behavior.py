from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ActionPrecheckBehavior"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ActionPrecheckBehavior:
    """
    ActionPrecheckBehavior

    Defines selection frequency behavior for an action or group.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/action-precheck-behavior
    """

    yes = CodeSystemConcept(
        {
            "code": "yes",
            "definition": 'An action with this behavior is one of the most frequent action that is, or should be, included by an end user, for the particular context in which the action occurs. The system displaying the action to the end user should consider "pre-checking" such an action as a convenience for the user.',
            "display": "Yes",
        }
    )
    """
    Yes

    An action with this behavior is one of the most frequent action that is, or should be, included by an end user, for the particular context in which the action occurs. The system displaying the action to the end user should consider "pre-checking" such an action as a convenience for the user.
    """

    no = CodeSystemConcept(
        {
            "code": "no",
            "definition": 'An action with this behavior is one of the less frequent actions included by the end user, for the particular context in which the action occurs. The system displaying the actions to the end user would typically not "pre-check" such an action.',
            "display": "No",
        }
    )
    """
    No

    An action with this behavior is one of the less frequent actions included by the end user, for the particular context in which the action occurs. The system displaying the actions to the end user would typically not "pre-check" such an action.
    """

    class Meta:
        resource = _resource
