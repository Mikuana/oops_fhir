from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["IssueSeverity"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class IssueSeverity:
    """
    IssueSeverity

    How the issue affects the success of the action.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/issue-severity
    """

    fatal = CodeSystemConcept(
        {
            "code": "fatal",
            "definition": "The issue caused the action to fail and no further checking could be performed.",
            "display": "Fatal",
        }
    )
    """
    Fatal

    The issue caused the action to fail and no further checking could be performed.
    """

    error = CodeSystemConcept(
        {
            "code": "error",
            "definition": "The issue is sufficiently important to cause the action to fail.",
            "display": "Error",
        }
    )
    """
    Error

    The issue is sufficiently important to cause the action to fail.
    """

    warning = CodeSystemConcept(
        {
            "code": "warning",
            "definition": "The issue is not important enough to cause the action to fail but may cause it to be performed suboptimally or in a way that is not as desired.",
            "display": "Warning",
        }
    )
    """
    Warning

    The issue is not important enough to cause the action to fail but may cause it to be performed suboptimally or in a way that is not as desired.
    """

    information = CodeSystemConcept(
        {
            "code": "information",
            "definition": "The issue has no relation to the degree of success of the action.",
            "display": "Information",
        }
    )
    """
    Information

    The issue has no relation to the degree of success of the action.
    """

    class Meta:
        resource = _resource
