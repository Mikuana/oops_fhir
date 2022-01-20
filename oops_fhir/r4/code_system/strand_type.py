from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["strandType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class strandType:
    """
    strandType

    Type for strand.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/strand-type
    """

    watson = CodeSystemConcept(
        {
            "code": "watson",
            "definition": "Watson strand of reference sequence.",
            "display": "Watson strand of referenceSeq",
        }
    )
    """
    Watson strand of referenceSeq

    Watson strand of reference sequence.
    """

    crick = CodeSystemConcept(
        {
            "code": "crick",
            "definition": "Crick strand of reference sequence.",
            "display": "Crick strand of referenceSeq",
        }
    )
    """
    Crick strand of referenceSeq

    Crick strand of reference sequence.
    """

    class Meta:
        resource = _resource
