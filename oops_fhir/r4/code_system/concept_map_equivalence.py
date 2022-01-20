from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ConceptMapEquivalence"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ConceptMapEquivalence:
    """
    ConceptMapEquivalence

    The degree of equivalence between concepts.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/concept-map-equivalence
    """

    relatedto = CodeSystemConcept(
        {
            "code": "relatedto",
            "concept": [
                {
                    "code": "equivalent",
                    "concept": [
                        {
                            "code": "equal",
                            "definition": "The definitions of the concepts are exactly the same (i.e. only grammatical differences) and structural implications of meaning are identical or irrelevant (i.e. intentionally identical).",
                            "display": "Equal",
                        }
                    ],
                    "definition": "The definitions of the concepts mean the same thing (including when structural implications of meaning are considered) (i.e. extensionally identical).",
                    "display": "Equivalent",
                },
                {
                    "code": "wider",
                    "definition": "The target mapping is wider in meaning than the source concept.",
                    "display": "Wider",
                },
                {
                    "code": "subsumes",
                    "definition": "The target mapping subsumes the meaning of the source concept (e.g. the source is-a target).",
                    "display": "Subsumes",
                },
                {
                    "code": "narrower",
                    "definition": "The target mapping is narrower in meaning than the source concept. The sense in which the mapping is narrower SHALL be described in the comments in this case, and applications should be careful when attempting to use these mappings operationally.",
                    "display": "Narrower",
                },
                {
                    "code": "specializes",
                    "definition": "The target mapping specializes the meaning of the source concept (e.g. the target is-a source).",
                    "display": "Specializes",
                },
                {
                    "code": "inexact",
                    "definition": "The target mapping overlaps with the source concept, but both source and target cover additional meaning, or the definitions are imprecise and it is uncertain whether they have the same boundaries to their meaning. The sense in which the mapping is inexact SHALL be described in the comments in this case, and applications should be careful when attempting to use these mappings operationally.",
                    "display": "Inexact",
                },
            ],
            "definition": "The concepts are related to each other, and have at least some overlap in meaning, but the exact relationship is not known.",
            "display": "Related To",
        }
    )
    """
    Related To

    The concepts are related to each other, and have at least some overlap in meaning, but the exact relationship is not known.
    """

    unmatched = CodeSystemConcept(
        {
            "code": "unmatched",
            "concept": [
                {
                    "code": "disjoint",
                    "definition": "This is an explicit assertion that there is no mapping between the source and target concept.",
                    "display": "Disjoint",
                }
            ],
            "definition": "There is no match for this concept in the target code system.",
            "display": "Unmatched",
        }
    )
    """
    Unmatched

    There is no match for this concept in the target code system.
    """

    class Meta:
        resource = _resource
