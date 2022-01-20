from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["HandlingConditionSet"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class HandlingConditionSet:
    """
    HandlingConditionSet

    Set of handling instructions prior testing of the specimen.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/handling-condition
    """

    room = CodeSystemConcept(
        {
            "code": "room",
            "definition": "room temperature.",
            "display": "room temperature",
        }
    )
    """
    room temperature

    room temperature.
    """

    refrigerated = CodeSystemConcept(
        {
            "code": "refrigerated",
            "definition": "refrigerated temperature.",
            "display": "refrigerated",
        }
    )
    """
    refrigerated

    refrigerated temperature.
    """

    frozen = CodeSystemConcept(
        {"code": "frozen", "definition": "frozen temperature.", "display": "frozen"}
    )
    """
    frozen

    frozen temperature.
    """

    class Meta:
        resource = _resource
