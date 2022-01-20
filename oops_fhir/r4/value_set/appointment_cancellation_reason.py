from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.appointment_cancellation_reason import (
    AppointmentCancellationReason as AppointmentCancellationReason_,
)


__all__ = ["AppointmentCancellationReason"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AppointmentCancellationReason(AppointmentCancellationReason_):
    """
    Appointment cancellation reason

    This example value set defines a set of reasons for the cancellation of
an appointment.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/appointment-cancellation-reason
    """

    class Meta:
        resource = _resource
