from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3Sequencing"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3Sequencing:
    """
    v3 Code System Sequencing

     Specifies sequence of sort order.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-Sequencing
    """

    a = CodeSystemConcept(
        {"code": "A", "definition": "Ascending sequence order.", "display": "Ascending"}
    )
    """
    Ascending

    Ascending sequence order.
    """

    d = CodeSystemConcept(
        {
            "code": "D",
            "definition": "Descending sequence order.",
            "display": "Descending",
        }
    )
    """
    Descending

    Descending sequence order.
    """

    n = CodeSystemConcept(
        {"code": "N", "definition": "No enforced sequence order.", "display": "None"}
    )
    """
    None

    No enforced sequence order.
    """

    class Meta:
        resource = _resource
