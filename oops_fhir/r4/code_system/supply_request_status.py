from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SupplyRequestStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SupplyRequestStatus:
    """
    SupplyRequestStatus

    Status of the supply request.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/supplyrequest-status
    """

    draft = CodeSystemConcept(
        {
            "code": "draft",
            "definition": "The request has been created but is not yet complete or ready for action.",
            "display": "Draft",
        }
    )
    """
    Draft

    The request has been created but is not yet complete or ready for action.
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "The request is ready to be acted upon.",
            "display": "Active",
        }
    )
    """
    Active

    The request is ready to be acted upon.
    """

    suspended = CodeSystemConcept(
        {
            "code": "suspended",
            "definition": "The authorization/request to act has been temporarily withdrawn but is expected to resume in the future.",
            "display": "Suspended",
        }
    )
    """
    Suspended

    The authorization/request to act has been temporarily withdrawn but is expected to resume in the future.
    """

    cancelled = CodeSystemConcept(
        {
            "code": "cancelled",
            "definition": "The authorization/request to act has been terminated prior to the full completion of the intended actions.  No further activity should occur.",
            "display": "Cancelled",
        }
    )
    """
    Cancelled

    The authorization/request to act has been terminated prior to the full completion of the intended actions.  No further activity should occur.
    """

    completed = CodeSystemConcept(
        {
            "code": "completed",
            "definition": "Activity against the request has been sufficiently completed to the satisfaction of the requester.",
            "display": "Completed",
        }
    )
    """
    Completed

    Activity against the request has been sufficiently completed to the satisfaction of the requester.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": 'This electronic record should never have existed, though it is possible that real-world decisions were based on it.  (If real-world activity has occurred, the status should be "cancelled" rather than "entered-in-error".).',
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    This electronic record should never have existed, though it is possible that real-world decisions were based on it.  (If real-world activity has occurred, the status should be "cancelled" rather than "entered-in-error".).
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
