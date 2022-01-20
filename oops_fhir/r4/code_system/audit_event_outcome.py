from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AuditEventOutcome"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AuditEventOutcome:
    """
    AuditEventOutcome

    Indicates whether the event succeeded or failed.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/audit-event-outcome
    """

    zero = CodeSystemConcept(
        {
            "code": "0",
            "definition": "The operation completed successfully (whether with warnings or not).",
            "display": "Success",
        }
    )
    """
    Success

    The operation completed successfully (whether with warnings or not).
    """

    four = CodeSystemConcept(
        {
            "code": "4",
            "definition": "The action was not successful due to some kind of minor failure (often equivalent to an HTTP 400 response).",
            "display": "Minor failure",
        }
    )
    """
    Minor failure

    The action was not successful due to some kind of minor failure (often equivalent to an HTTP 400 response).
    """

    eight = CodeSystemConcept(
        {
            "code": "8",
            "definition": "The action was not successful due to some kind of unexpected error (often equivalent to an HTTP 500 response).",
            "display": "Serious failure",
        }
    )
    """
    Serious failure

    The action was not successful due to some kind of unexpected error (often equivalent to an HTTP 500 response).
    """

    one2 = CodeSystemConcept(
        {
            "code": "12",
            "definition": "An error of such magnitude occurred that the system is no longer available for use (i.e. the system died).",
            "display": "Major failure",
        }
    )
    """
    Major failure

    An error of such magnitude occurred that the system is no longer available for use (i.e. the system died).
    """

    class Meta:
        resource = _resource
