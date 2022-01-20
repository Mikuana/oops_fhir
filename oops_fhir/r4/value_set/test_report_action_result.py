from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.test_report_action_result import (
    TestReportActionResult as TestReportActionResult_,
)


__all__ = ["TestReportActionResult"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TestReportActionResult(TestReportActionResult_):
    """
    TestReportActionResult

    The results of executing an action.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/report-action-result-codes
    """

    class Meta:
        resource = _resource
