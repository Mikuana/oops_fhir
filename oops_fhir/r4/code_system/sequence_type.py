from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["sequenceType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class sequenceType:
    """
    sequenceType

    Type if a sequence -- DNA, RNA, or amino acid sequence.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/sequence-type
    """

    aa = CodeSystemConcept(
        {"code": "aa", "definition": "Amino acid sequence.", "display": "AA Sequence"}
    )
    """
    AA Sequence

    Amino acid sequence.
    """

    dna = CodeSystemConcept(
        {"code": "dna", "definition": "DNA Sequence.", "display": "DNA Sequence"}
    )
    """
    DNA Sequence

    DNA Sequence.
    """

    rna = CodeSystemConcept(
        {"code": "rna", "definition": "RNA Sequence.", "display": "RNA Sequence"}
    )
    """
    RNA Sequence

    RNA Sequence.
    """

    class Meta:
        resource = _resource
