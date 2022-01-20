from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MeasureReportStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MeasureReportStatus:
    """
    MeasureReportStatus

    The status of the measure report.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/measure-report-status
    """

    complete = CodeSystemConcept(
        {
            "code": "complete",
            "definition": "The report is complete and ready for use.",
            "display": "Complete",
        }
    )
    """
    Complete

    The report is complete and ready for use.
    """

    pending = CodeSystemConcept(
        {
            "code": "pending",
            "definition": "The report is currently being generated.",
            "display": "Pending",
        }
    )
    """
    Pending

    The report is currently being generated.
    """

    error = CodeSystemConcept(
        {
            "code": "error",
            "definition": "An error occurred attempting to generate the report.",
            "display": "Error",
        }
    )
    """
    Error

    An error occurred attempting to generate the report.
    """

    class Meta:
        resource = _resource
