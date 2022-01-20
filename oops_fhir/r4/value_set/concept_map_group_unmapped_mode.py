from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.concept_map_group_unmapped_mode import (
    ConceptMapGroupUnmappedMode as ConceptMapGroupUnmappedMode_,
)


__all__ = ["ConceptMapGroupUnmappedMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConceptMapGroupUnmappedMode(ConceptMapGroupUnmappedMode_):
    """
    ConceptMapGroupUnmappedMode

    Defines which action to take if there is no match in the group.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/conceptmap-unmapped-mode
    """

    class Meta:
        resource = _resource
