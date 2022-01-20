from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.participant_required import (
    ParticipantRequired as ParticipantRequired_,
)


__all__ = ["ParticipantRequired"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ParticipantRequired(ParticipantRequired_):
    """
    ParticipantRequired

    Is the Participant required to attend the appointment.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/participantrequired
    """

    class Meta:
        resource = _resource
