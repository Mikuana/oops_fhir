from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.provenance_participant_role import (
    ProvenanceParticipantRole as ProvenanceParticipantRole_,
)


__all__ = ["ProvenanceParticipantRole"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ProvenanceParticipantRole(ProvenanceParticipantRole_):
    """
    Provenance participant role

    The role that a provenance participant played

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/provenance-agent-role
    """

    class Meta:
        resource = _resource
