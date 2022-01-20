from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AppointmentStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AppointmentStatus:
    """
    AppointmentStatus

    The free/busy status of an appointment.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/appointmentstatus
    """

    proposed = CodeSystemConcept(
        {
            "code": "proposed",
            "definition": "None of the participant(s) have finalized their acceptance of the appointment request, and the start/end time might not be set yet.",
            "display": "Proposed",
        }
    )
    """
    Proposed

    None of the participant(s) have finalized their acceptance of the appointment request, and the start/end time might not be set yet.
    """

    pending = CodeSystemConcept(
        {
            "code": "pending",
            "definition": "Some or all of the participant(s) have not finalized their acceptance of the appointment request.",
            "display": "Pending",
        }
    )
    """
    Pending

    Some or all of the participant(s) have not finalized their acceptance of the appointment request.
    """

    booked = CodeSystemConcept(
        {
            "code": "booked",
            "definition": "All participant(s) have been considered and the appointment is confirmed to go ahead at the date/times specified.",
            "display": "Booked",
        }
    )
    """
    Booked

    All participant(s) have been considered and the appointment is confirmed to go ahead at the date/times specified.
    """

    arrived = CodeSystemConcept(
        {
            "code": "arrived",
            "definition": "The patient/patients has/have arrived and is/are waiting to be seen.",
            "display": "Arrived",
        }
    )
    """
    Arrived

    The patient/patients has/have arrived and is/are waiting to be seen.
    """

    fulfilled = CodeSystemConcept(
        {
            "code": "fulfilled",
            "definition": "The planning stages of the appointment are now complete, the encounter resource will exist and will track further status changes. Note that an encounter may exist before the appointment status is fulfilled for many reasons.",
            "display": "Fulfilled",
        }
    )
    """
    Fulfilled

    The planning stages of the appointment are now complete, the encounter resource will exist and will track further status changes. Note that an encounter may exist before the appointment status is fulfilled for many reasons.
    """

    cancelled = CodeSystemConcept(
        {
            "code": "cancelled",
            "definition": "The appointment has been cancelled.",
            "display": "Cancelled",
        }
    )
    """
    Cancelled

    The appointment has been cancelled.
    """

    noshow = CodeSystemConcept(
        {
            "code": "noshow",
            "definition": "Some or all of the participant(s) have not/did not appear for the appointment (usually the patient).",
            "display": "No Show",
        }
    )
    """
    No Show

    Some or all of the participant(s) have not/did not appear for the appointment (usually the patient).
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "This instance should not have been part of this patient's medical record.",
            "display": "Entered in error",
        }
    )
    """
    Entered in error

    This instance should not have been part of this patient's medical record.
    """

    checked_in = CodeSystemConcept(
        {
            "code": "checked-in",
            "definition": "When checked in, all pre-encounter administrative work is complete, and the encounter may begin. (where multiple patients are involved, they are all present).",
            "display": "Checked In",
        }
    )
    """
    Checked In

    When checked in, all pre-encounter administrative work is complete, and the encounter may begin. (where multiple patients are involved, they are all present).
    """

    waitlist = CodeSystemConcept(
        {
            "code": "waitlist",
            "definition": "The appointment has been placed on a waitlist, to be scheduled/confirmed in the future when a slot/service is available.\nA specific time might or might not be pre-allocated.",
            "display": "Waitlisted",
        }
    )
    """
    Waitlisted

    The appointment has been placed on a waitlist, to be scheduled/confirmed in the future when a slot/service is available.
A specific time might or might not be pre-allocated.
    """

    class Meta:
        resource = _resource
