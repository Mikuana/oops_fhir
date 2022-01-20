from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DiagnosticReportStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DiagnosticReportStatus:
    """
    DiagnosticReportStatus

    The status of the diagnostic report.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/diagnostic-report-status
    """

    registered = CodeSystemConcept(
        {
            "code": "registered",
            "definition": "The existence of the report is registered, but there is nothing yet available.",
            "display": "Registered",
        }
    )
    """
    Registered

    The existence of the report is registered, but there is nothing yet available.
    """

    partial = CodeSystemConcept(
        {
            "code": "partial",
            "concept": [
                {
                    "code": "preliminary",
                    "definition": "Verified early results are available, but not all  results are final.",
                    "display": "Preliminary",
                }
            ],
            "definition": "This is a partial (e.g. initial, interim or preliminary) report: data in the report may be incomplete or unverified.",
            "display": "Partial",
        }
    )
    """
    Partial

    This is a partial (e.g. initial, interim or preliminary) report: data in the report may be incomplete or unverified.
    """

    final = CodeSystemConcept(
        {
            "code": "final",
            "definition": "The report is complete and verified by an authorized person.",
            "display": "Final",
        }
    )
    """
    Final

    The report is complete and verified by an authorized person.
    """

    amended = CodeSystemConcept(
        {
            "code": "amended",
            "concept": [
                {
                    "code": "corrected",
                    "definition": "Subsequent to being final, the report has been modified  to correct an error in the report or referenced results.",
                    "display": "Corrected",
                },
                {
                    "code": "appended",
                    "definition": "Subsequent to being final, the report has been modified by adding new content. The existing content is unchanged.",
                    "display": "Appended",
                },
            ],
            "definition": "Subsequent to being final, the report has been modified.  This includes any change in the results, diagnosis, narrative text, or other content of a report that has been issued.",
            "display": "Amended",
        }
    )
    """
    Amended

    Subsequent to being final, the report has been modified.  This includes any change in the results, diagnosis, narrative text, or other content of a report that has been issued.
    """

    cancelled = CodeSystemConcept(
        {
            "code": "cancelled",
            "definition": 'The report is unavailable because the measurement was not started or not completed (also sometimes called "aborted").',
            "display": "Cancelled",
        }
    )
    """
    Cancelled

    The report is unavailable because the measurement was not started or not completed (also sometimes called "aborted").
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": 'The report has been withdrawn following a previous final release.  This electronic record should never have existed, though it is possible that real-world decisions were based on it. (If real-world activity has occurred, the status should be "cancelled" rather than "entered-in-error".).',
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The report has been withdrawn following a previous final release.  This electronic record should never have existed, though it is possible that real-world decisions were based on it. (If real-world activity has occurred, the status should be "cancelled" rather than "entered-in-error".).
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": 'The authoring/source system does not know which of the status values currently applies for this observation. Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, but the authoring/source system does not know which.',
            "display": "Unknown",
        }
    )
    """
    Unknown

    The authoring/source system does not know which of the status values currently applies for this observation. Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, but the authoring/source system does not know which.
    """

    class Meta:
        resource = _resource
