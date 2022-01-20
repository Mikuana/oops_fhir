from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.concept_map_equivalence import (
    ConceptMapEquivalence as ConceptMapEquivalence_,
)


__all__ = ["ConceptMapEquivalence"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConceptMapEquivalence(ConceptMapEquivalence_):
    """
    ConceptMapEquivalence

    The degree of equivalence between concepts.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/concept-map-equivalence
    """

    class Meta:
        resource = _resource
