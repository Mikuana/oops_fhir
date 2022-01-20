from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3MapRelationship"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3MapRelationship:
    """
    v3 Code System MapRelationship

     The closeness or quality of the mapping between the HL7 concept (as
represented by the HL7 concept identifier) and the source coding system.
The values are patterned after the similar relationships used in the
UMLS Metathesaurus. Because the HL7 coding sy

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-MapRelationship
    """

    bt = CodeSystemConcept(
        {
            "code": "BT",
            "definition": "The first concept is at a more abstract level than the second concept.  For example, Hepatitis is broader than Hepatitis A, and endocrine disease is broader than Diabetes Mellitus.  Broader than is the opposite of the narrower than relationship.",
            "display": "Broader Than",
        }
    )
    """
    Broader Than

    The first concept is at a more abstract level than the second concept.  For example, Hepatitis is broader than Hepatitis A, and endocrine disease is broader than Diabetes Mellitus.  Broader than is the opposite of the narrower than relationship.
    """

    e = CodeSystemConcept(
        {
            "code": "E",
            "definition": "The two concepts have identical meaning.",
            "display": "Exact",
        }
    )
    """
    Exact

    The two concepts have identical meaning.
    """

    nt = CodeSystemConcept(
        {
            "code": "NT",
            "definition": "The first concept is at a more detailed level than the second concept.  For example, Pennicillin G is narrower than Pennicillin, and vellus hair is narrower than hair.  Narrower than is the opposite of broader than.",
            "display": "Narrower Than",
        }
    )
    """
    Narrower Than

    The first concept is at a more detailed level than the second concept.  For example, Pennicillin G is narrower than Pennicillin, and vellus hair is narrower than hair.  Narrower than is the opposite of broader than.
    """

    class Meta:
        resource = _resource
