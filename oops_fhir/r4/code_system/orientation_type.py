from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["orientationType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class orientationType:
    """
    orientationType

    Type for orientation.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/orientation-type
    """

    sense = CodeSystemConcept(
        {
            "code": "sense",
            "definition": "Sense orientation of reference sequence.",
            "display": "Sense orientation of referenceSeq",
        }
    )
    """
    Sense orientation of referenceSeq

    Sense orientation of reference sequence.
    """

    antisense = CodeSystemConcept(
        {
            "code": "antisense",
            "definition": "Antisense orientation of reference sequence.",
            "display": "Antisense orientation of referenceSeq",
        }
    )
    """
    Antisense orientation of referenceSeq

    Antisense orientation of reference sequence.
    """

    class Meta:
        resource = _resource
