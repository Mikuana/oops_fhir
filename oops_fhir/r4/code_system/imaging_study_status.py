from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ImagingStudyStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ImagingStudyStatus:
    """
    ImagingStudyStatus

    The status of the ImagingStudy.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/imagingstudy-status
    """

    registered = CodeSystemConcept(
        {
            "code": "registered",
            "definition": "The existence of the imaging study is registered, but there is nothing yet available.",
            "display": "Registered",
        }
    )
    """
    Registered

    The existence of the imaging study is registered, but there is nothing yet available.
    """

    available = CodeSystemConcept(
        {
            "code": "available",
            "definition": "At least one instance has been associated with this imaging study.",
            "display": "Available",
        }
    )
    """
    Available

    At least one instance has been associated with this imaging study.
    """

    cancelled = CodeSystemConcept(
        {
            "code": "cancelled",
            "definition": 'The imaging study is unavailable because the imaging study was not started or not completed (also sometimes called "aborted").',
            "display": "Cancelled",
        }
    )
    """
    Cancelled

    The imaging study is unavailable because the imaging study was not started or not completed (also sometimes called "aborted").
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": 'The imaging study has been withdrawn following a previous final release.  This electronic record should never have existed, though it is possible that real-world decisions were based on it. (If real-world activity has occurred, the status should be "cancelled" rather than "entered-in-error".).',
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The imaging study has been withdrawn following a previous final release.  This electronic record should never have existed, though it is possible that real-world decisions were based on it. (If real-world activity has occurred, the status should be "cancelled" rather than "entered-in-error".).
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": 'The system does not know which of the status values currently applies for this request. Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, it\'s just not known which one.',
            "display": "Unknown",
        }
    )
    """
    Unknown

    The system does not know which of the status values currently applies for this request. Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, it's just not known which one.
    """

    class Meta:
        resource = _resource
