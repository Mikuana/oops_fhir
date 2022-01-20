from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.diagnostic_report_status import (
    DiagnosticReportStatus as DiagnosticReportStatus_,
)


__all__ = ["DiagnosticReportStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DiagnosticReportStatus(DiagnosticReportStatus_):
    """
    DiagnosticReportStatus

    The status of the diagnostic report.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/diagnostic-report-status
    """

    class Meta:
        resource = _resource
