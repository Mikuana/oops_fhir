from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["RequestStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class RequestStatus:
    """
    RequestStatus

    Codes identifying the lifecycle stage of a request.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/request-status
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
            "definition": "The request is in force and ready to be acted upon.",
            "display": "Active",
        }
    )
    """
    Active

    The request is in force and ready to be acted upon.
    """

    on_hold = CodeSystemConcept(
        {
            "code": "on-hold",
            "definition": "The request (and any implicit authorization to act) has been temporarily withdrawn but is expected to resume in the future.",
            "display": "On Hold",
        }
    )
    """
    On Hold

    The request (and any implicit authorization to act) has been temporarily withdrawn but is expected to resume in the future.
    """

    revoked = CodeSystemConcept(
        {
            "code": "revoked",
            "definition": "The request (and any implicit authorization to act) has been terminated prior to the known full completion of the intended actions.  No further activity should occur.",
            "display": "Revoked",
        }
    )
    """
    Revoked

    The request (and any implicit authorization to act) has been terminated prior to the known full completion of the intended actions.  No further activity should occur.
    """

    completed = CodeSystemConcept(
        {
            "code": "completed",
            "definition": "The activity described by the request has been fully performed.  No further activity will occur.",
            "display": "Completed",
        }
    )
    """
    Completed

    The activity described by the request has been fully performed.  No further activity will occur.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": 'This request should never have existed and should be considered \'void\'.  (It is possible that real-world decisions were based on it.  If real-world activity has occurred, the status should be "revoked" rather than "entered-in-error".).',
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    This request should never have existed and should be considered 'void'.  (It is possible that real-world decisions were based on it.  If real-world activity has occurred, the status should be "revoked" rather than "entered-in-error".).
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": 'The authoring/source system does not know which of the status values currently applies for this request.  Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply,  but the authoring/source system does not know which.',
            "display": "Unknown",
        }
    )
    """
    Unknown

    The authoring/source system does not know which of the status values currently applies for this request.  Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply,  but the authoring/source system does not know which.
    """

    class Meta:
        resource = _resource
