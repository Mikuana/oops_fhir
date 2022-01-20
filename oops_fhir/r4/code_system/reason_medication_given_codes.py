from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ReasonMedicationGivenCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ReasonMedicationGivenCodes:
    """
    Reason Medication Given Codes

    This value set is provided as an example. The value set to instantiate
this attribute should be drawn from a robust terminology code system
that consists of or contains concepts to support the medication process.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/reason-medication-given
    """

    a = CodeSystemConcept(
        {"code": "a", "definition": "No reason known.", "display": "None"}
    )
    """
    None

    No reason known.
    """

    b = CodeSystemConcept(
        {
            "code": "b",
            "definition": "The administration was following an ordered protocol.",
            "display": "Given as Ordered",
        }
    )
    """
    Given as Ordered

    The administration was following an ordered protocol.
    """

    c = CodeSystemConcept(
        {
            "code": "c",
            "definition": "The administration was needed to treat an emergency.",
            "display": "Emergency",
        }
    )
    """
    Emergency

    The administration was needed to treat an emergency.
    """

    class Meta:
        resource = _resource
