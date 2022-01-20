from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["TestReportActionResult"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class TestReportActionResult:
    """
    TestReportActionResult

    The results of executing an action.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/report-action-result-codes
    """

    pass_ = CodeSystemConcept(
        {"code": "pass", "definition": "The action was successful.", "display": "Pass"}
    )
    """
    Pass

    The action was successful.
    """

    skip = CodeSystemConcept(
        {"code": "skip", "definition": "The action was skipped.", "display": "Skip"}
    )
    """
    Skip

    The action was skipped.
    """

    fail = CodeSystemConcept(
        {"code": "fail", "definition": "The action failed.", "display": "Fail"}
    )
    """
    Fail

    The action failed.
    """

    warning = CodeSystemConcept(
        {
            "code": "warning",
            "definition": "The action passed but with warnings.",
            "display": "Warning",
        }
    )
    """
    Warning

    The action passed but with warnings.
    """

    error = CodeSystemConcept(
        {
            "code": "error",
            "definition": "The action encountered a fatal error and the engine was unable to process.",
            "display": "Error",
        }
    )
    """
    Error

    The action encountered a fatal error and the engine was unable to process.
    """

    class Meta:
        resource = _resource
