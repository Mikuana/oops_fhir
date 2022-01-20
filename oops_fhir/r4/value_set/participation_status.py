from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.participation_status import (
    ParticipationStatus as ParticipationStatus_,
)


__all__ = ["ParticipationStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ParticipationStatus(ParticipationStatus_):
    """
    ParticipationStatus

    The Participation status of an appointment.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/participationstatus
    """

    class Meta:
        resource = _resource
