from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MaxOccurs"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MaxOccurs:
    """
    MaxOccurs

    Flags an element as having unlimited repetitions.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/question-max-occurs
    """

    asterisk = CodeSystemConcept(
        {
            "code": "*",
            "definition": "Element can repeat an unlimited number of times.",
            "display": "Repeating",
        }
    )
    """
    Repeating

    Element can repeat an unlimited number of times.
    """

    class Meta:
        resource = _resource
