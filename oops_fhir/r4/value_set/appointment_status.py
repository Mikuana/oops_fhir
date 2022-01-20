from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.appointment_status import (
    AppointmentStatus as AppointmentStatus_,
)


__all__ = ["AppointmentStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AppointmentStatus(AppointmentStatus_):
    """
    AppointmentStatus

    The free/busy status of an appointment.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/appointmentstatus
    """

    class Meta:
        resource = _resource
