from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.provenance_entity_role import (
    ProvenanceEntityRole as ProvenanceEntityRole_,
)


__all__ = ["ProvenanceEntityRole"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ProvenanceEntityRole(ProvenanceEntityRole_):
    """
    ProvenanceEntityRole

    How an entity was used in an activity.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/provenance-entity-role
    """

    class Meta:
        resource = _resource
