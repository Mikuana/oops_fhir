from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ConceptSubsumptionOutcome"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ConceptSubsumptionOutcome:
    """
    ConceptSubsumptionOutcome

    The subsumption relationship between code/Coding "A" and code/Coding
"B". There are 4 possible codes to be returned: equivalent, subsumes,
subsumed-by, and not-subsumed. If the server is unable to determine the
relationship between the codes/Codings, then it returns an error (i.e.
an OperationOutcome).

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/concept-subsumption-outcome
    """

    equivalent = CodeSystemConcept(
        {
            "code": "equivalent",
            "definition": "The two concepts are equivalent (have the same properties).",
            "display": "Equivalent",
        }
    )
    """
    Equivalent

    The two concepts are equivalent (have the same properties).
    """

    subsumes = CodeSystemConcept(
        {
            "code": "subsumes",
            "definition": 'Coding/code "A" subsumes Coding/code "B" (e.g. B has all the properties A has, and some of it\'s own).',
            "display": "Subsumes",
        }
    )
    """
    Subsumes

    Coding/code "A" subsumes Coding/code "B" (e.g. B has all the properties A has, and some of it's own).
    """

    subsumed_by = CodeSystemConcept(
        {
            "code": "subsumed-by",
            "definition": 'Coding/code "A" is subsumed by Coding/code "B" (e.g. A has all the properties B has, and some of it\'s own).',
            "display": "Subsumed-By",
        }
    )
    """
    Subsumed-By

    Coding/code "A" is subsumed by Coding/code "B" (e.g. A has all the properties B has, and some of it's own).
    """

    not_subsumed = CodeSystemConcept(
        {
            "code": "not-subsumed",
            "definition": 'Coding/code "A" and Coding/code "B" are disjoint (e.g. each has propeties that the other doesn\'t have).',
            "display": "Not-Subsumed",
        }
    )
    """
    Not-Subsumed

    Coding/code "A" and Coding/code "B" are disjoint (e.g. each has propeties that the other doesn't have).
    """

    class Meta:
        resource = _resource
