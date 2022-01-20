from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["medicationrequestStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class medicationrequestStatus:
    """
    Medicationrequest  status

    MedicationRequest Status Codes

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/CodeSystem/medicationrequest-status
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "The prescription is 'actionable', but not all actions that are implied by it have occurred yet.",
            "display": "Active",
        }
    )
    """
    Active

    The prescription is 'actionable', but not all actions that are implied by it have occurred yet.
    """

    on_hold = CodeSystemConcept(
        {
            "code": "on-hold",
            "definition": "Actions implied by the prescription are to be temporarily halted, but are expected to continue later.  May also be called 'suspended'.",
            "display": "On Hold",
        }
    )
    """
    On Hold

    Actions implied by the prescription are to be temporarily halted, but are expected to continue later.  May also be called 'suspended'.
    """

    cancelled = CodeSystemConcept(
        {
            "code": "cancelled",
            "definition": "The prescription has been withdrawn before any administrations have occurred",
            "display": "Cancelled",
        }
    )
    """
    Cancelled

    The prescription has been withdrawn before any administrations have occurred
    """

    completed = CodeSystemConcept(
        {
            "code": "completed",
            "definition": "All actions that are implied by the prescription have occurred.",
            "display": "Completed",
        }
    )
    """
    Completed

    All actions that are implied by the prescription have occurred.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "Some of the actions that are implied by the medication request may have occurred.  For example, the medication may have been dispensed and the patient may have taken some of the medication.  Clinical decision support systems should take this status into account",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    Some of the actions that are implied by the medication request may have occurred.  For example, the medication may have been dispensed and the patient may have taken some of the medication.  Clinical decision support systems should take this status into account
    """

    stopped = CodeSystemConcept(
        {
            "code": "stopped",
            "definition": "Actions implied by the prescription are to be permanently halted, before all of the administrations occurred. This should not be used if the original order was entered in error",
            "display": "Stopped",
        }
    )
    """
    Stopped

    Actions implied by the prescription are to be permanently halted, before all of the administrations occurred. This should not be used if the original order was entered in error
    """

    draft = CodeSystemConcept(
        {
            "code": "draft",
            "definition": "The prescription is not yet 'actionable', e.g. it is a work in progress, requires sign-off, verification\xa0or\xa0needs to be run through decision support process.",
            "display": "Draft",
        }
    )
    """
    Draft

    The prescription is not yet 'actionable', e.g. it is a work in progress, requires sign-off, verification or needs to be run through decision support process.
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": "The authoring/source system does not know which of the status values currently applies for this observation. Note: This concept is not to be used for 'other' - one of the listed statuses is presumed to apply, but the authoring/source system does not know which.",
            "display": "Unknown",
        }
    )
    """
    Unknown

    The authoring/source system does not know which of the status values currently applies for this observation. Note: This concept is not to be used for 'other' - one of the listed statuses is presumed to apply, but the authoring/source system does not know which.
    """

    class Meta:
        resource = _resource
