from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExampleDiagnosisRelatedGroupCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExampleDiagnosisRelatedGroupCodes:
    """
    Example Diagnosis Related Group Codes

    This value set includes example Diagnosis Related Group codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/ex-diagnosisrelatedgroup
    """

    one00 = CodeSystemConcept(
        {
            "code": "100",
            "definition": "Normal Vaginal Delivery.",
            "display": "Normal Vaginal Delivery",
        }
    )
    """
    Normal Vaginal Delivery

    Normal Vaginal Delivery.
    """

    one01 = CodeSystemConcept(
        {
            "code": "101",
            "definition": "Appendectomy without rupture or other complications.",
            "display": "Appendectomy - uncomplicated",
        }
    )
    """
    Appendectomy - uncomplicated

    Appendectomy without rupture or other complications.
    """

    three00 = CodeSystemConcept(
        {
            "code": "300",
            "definition": "Emergency department treatment of a tooth abscess.",
            "display": "Tooth abscess",
        }
    )
    """
    Tooth abscess

    Emergency department treatment of a tooth abscess.
    """

    four00 = CodeSystemConcept(
        {
            "code": "400",
            "definition": "Head trauma - concussion.",
            "display": "Head trauma - concussion",
        }
    )
    """
    Head trauma - concussion

    Head trauma - concussion.
    """

    class Meta:
        resource = _resource
