from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["TestReportStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class TestReportStatus:
    """
    TestReportStatus

    The current status of the test report.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/report-status-codes
    """

    completed = CodeSystemConcept(
        {
            "code": "completed",
            "definition": "All test operations have completed.",
            "display": "Completed",
        }
    )
    """
    Completed

    All test operations have completed.
    """

    in_progress = CodeSystemConcept(
        {
            "code": "in-progress",
            "definition": "A test operations is currently executing.",
            "display": "In Progress",
        }
    )
    """
    In Progress

    A test operations is currently executing.
    """

    waiting = CodeSystemConcept(
        {
            "code": "waiting",
            "definition": "A test operation is waiting for an external client request.",
            "display": "Waiting",
        }
    )
    """
    Waiting

    A test operation is waiting for an external client request.
    """

    stopped = CodeSystemConcept(
        {
            "code": "stopped",
            "definition": "The test script execution was manually stopped.",
            "display": "Stopped",
        }
    )
    """
    Stopped

    The test script execution was manually stopped.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "This test report was entered or created in error.",
            "display": "Entered In Error",
        }
    )
    """
    Entered In Error

    This test report was entered or created in error.
    """

    class Meta:
        resource = _resource
