from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ActionParticipantType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ActionParticipantType:
    """
    ActionParticipantType

    The type of participant for the action.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/action-participant-type
    """

    patient = CodeSystemConcept(
        {
            "code": "patient",
            "definition": "The participant is the patient under evaluation.",
            "display": "Patient",
        }
    )
    """
    Patient

    The participant is the patient under evaluation.
    """

    practitioner = CodeSystemConcept(
        {
            "code": "practitioner",
            "definition": "The participant is a practitioner involved in the patient's care.",
            "display": "Practitioner",
        }
    )
    """
    Practitioner

    The participant is a practitioner involved in the patient's care.
    """

    related_person = CodeSystemConcept(
        {
            "code": "related-person",
            "definition": "The participant is a person related to the patient.",
            "display": "Related Person",
        }
    )
    """
    Related Person

    The participant is a person related to the patient.
    """

    device = CodeSystemConcept(
        {
            "code": "device",
            "definition": "The participant is a system or device used in the care of the patient.",
            "display": "Device",
        }
    )
    """
    Device

    The participant is a system or device used in the care of the patient.
    """

    class Meta:
        resource = _resource
