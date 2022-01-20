from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.action_participant_type import (
    ActionParticipantType as ActionParticipantType_,
)


__all__ = ["ActionParticipantType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ActionParticipantType(ActionParticipantType_):
    """
    ActionParticipantType

    The type of participant for the action.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/action-participant-type
    """

    class Meta:
        resource = _resource
