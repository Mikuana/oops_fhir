from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.provenance_participant_type import (
    ProvenanceParticipantType as ProvenanceParticipantType_,
)


__all__ = ["ProvenanceParticipantType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ProvenanceParticipantType(ProvenanceParticipantType_):
    """
    Provenance participant type

    The type of participation a provenance participant.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/provenance-agent-type
    """

    class Meta:
        resource = _resource
