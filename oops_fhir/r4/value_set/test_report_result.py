from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.test_report_result import (
    TestReportResult as TestReportResult_,
)


__all__ = ["TestReportResult"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TestReportResult(TestReportResult_):
    """
    TestReportResult

    The reported execution result.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/report-result-codes
    """

    class Meta:
        resource = _resource
