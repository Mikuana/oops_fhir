from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["TestReportResult"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class TestReportResult:
    """
    TestReportResult

    The reported execution result.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/report-result-codes
    """

    pass_ = CodeSystemConcept(
        {
            "code": "pass",
            "definition": "All test operations successfully passed all asserts.",
            "display": "Pass",
        }
    )
    """
    Pass

    All test operations successfully passed all asserts.
    """

    fail = CodeSystemConcept(
        {
            "code": "fail",
            "definition": "One or more test operations failed one or more asserts.",
            "display": "Fail",
        }
    )
    """
    Fail

    One or more test operations failed one or more asserts.
    """

    pending = CodeSystemConcept(
        {
            "code": "pending",
            "definition": "One or more test operations is pending execution completion.",
            "display": "Pending",
        }
    )
    """
    Pending

    One or more test operations is pending execution completion.
    """

    class Meta:
        resource = _resource
