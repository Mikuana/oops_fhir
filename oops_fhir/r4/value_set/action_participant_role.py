from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ActionParticipantRole"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ActionParticipantRole(ValueSet):
    """
    Action participant role

    Either a practitioner role or a relationship type.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/action-participant-role
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
