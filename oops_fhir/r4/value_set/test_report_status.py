from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.test_report_status import (
    TestReportStatus as TestReportStatus_,
)


__all__ = ["TestReportStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TestReportStatus(TestReportStatus_):
    """
    TestReportStatus

    The current status of the test report.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/report-status-codes
    """

    class Meta:
        resource = _resource
