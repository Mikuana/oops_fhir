from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ProvenanceEntityRole"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ProvenanceEntityRole:
    """
    ProvenanceEntityRole

    How an entity was used in an activity.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/provenance-entity-role
    """

    derivation = CodeSystemConcept(
        {
            "code": "derivation",
            "concept": [
                {
                    "code": "revision",
                    "definition": "A derivation for which the resulting entity is a revised version of some original.",
                    "display": "Revision",
                },
                {
                    "code": "quotation",
                    "definition": "The repeat of (some or all of) an entity, such as text or image, by someone who might or might not be its original author.",
                    "display": "Quotation",
                },
                {
                    "code": "source",
                    "definition": "A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight.",
                    "display": "Source",
                },
                {
                    "code": "removal",
                    "definition": "A derivation for which the entity is removed from accessibility usually through the use of the Delete operation.",
                    "display": "Removal",
                },
            ],
            "definition": "A transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.",
            "display": "Derivation",
        }
    )
    """
    Derivation

    A transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.
    """

    class Meta:
        resource = _resource
