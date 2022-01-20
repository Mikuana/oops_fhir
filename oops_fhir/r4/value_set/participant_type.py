from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_participation_type import v3ParticipationType

from oops_fhir.r4.code_system.participant_type import (
    ParticipantType as ParticipantType_,
)


__all__ = ["ParticipantType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ParticipantType(ValueSet):
    """
    Participant type

    This value set defines a set of codes that can be used to indicate how
an individual participates in an encounter.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/encounter-participant-type
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
