from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.measure_report_status import (
    MeasureReportStatus as MeasureReportStatus_,
)


__all__ = ["MeasureReportStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MeasureReportStatus(MeasureReportStatus_):
    """
    MeasureReportStatus

    The status of the measure report.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/measure-report-status
    """

    class Meta:
        resource = _resource
