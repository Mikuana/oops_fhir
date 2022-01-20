from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MedicationDispenseStatusCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MedicationDispenseStatusCodes:
    """
    Medication dispense  status  codes

    MedicationDispense Status Codes

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/medicationdispense-status
    """

    preparation = CodeSystemConcept(
        {
            "code": "preparation",
            "definition": "The core event has not started yet, but some staging activities have begun (e.g. initial compounding or packaging of medication). Preparation stages may be tracked for billing purposes.",
            "display": "Preparation",
        }
    )
    """
    Preparation

    The core event has not started yet, but some staging activities have begun (e.g. initial compounding or packaging of medication). Preparation stages may be tracked for billing purposes.
    """

    in_progress = CodeSystemConcept(
        {
            "code": "in-progress",
            "definition": "The dispensed product is ready for pickup.",
            "display": "In Progress",
        }
    )
    """
    In Progress

    The dispensed product is ready for pickup.
    """

    cancelled = CodeSystemConcept(
        {
            "code": "cancelled",
            "definition": "The dispensed product was not and will never be picked up by the patient.",
            "display": "Cancelled",
        }
    )
    """
    Cancelled

    The dispensed product was not and will never be picked up by the patient.
    """

    on_hold = CodeSystemConcept(
        {
            "code": "on-hold",
            "definition": "The dispense process is paused while waiting for an external event to reactivate the dispense.  For example, new stock has arrived or the prescriber has called.",
            "display": "On Hold",
        }
    )
    """
    On Hold

    The dispense process is paused while waiting for an external event to reactivate the dispense.  For example, new stock has arrived or the prescriber has called.
    """

    completed = CodeSystemConcept(
        {
            "code": "completed",
            "definition": "The dispensed product has been picked up.",
            "display": "Completed",
        }
    )
    """
    Completed

    The dispensed product has been picked up.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The dispense was entered in error and therefore nullified.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The dispense was entered in error and therefore nullified.
    """

    stopped = CodeSystemConcept(
        {
            "code": "stopped",
            "definition": "Actions implied by the dispense have been permanently halted, before all of them occurred.",
            "display": "Stopped",
        }
    )
    """
    Stopped

    Actions implied by the dispense have been permanently halted, before all of them occurred.
    """

    declined = CodeSystemConcept(
        {
            "code": "declined",
            "definition": "The dispense was declined and not performed.",
            "display": "Declined",
        }
    )
    """
    Declined

    The dispense was declined and not performed.
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": "The authoring system does not know which of the status values applies for this medication dispense.  Note: this concept is not to be used for other - one of the listed statuses is presumed to apply, it's just now known which one.",
            "display": "Unknown",
        }
    )
    """
    Unknown

    The authoring system does not know which of the status values applies for this medication dispense.  Note: this concept is not to be used for other - one of the listed statuses is presumed to apply, it's just now known which one.
    """

    class Meta:
        resource = _resource
