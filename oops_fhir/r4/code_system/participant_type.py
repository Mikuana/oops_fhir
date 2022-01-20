from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ParticipantType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ParticipantType:
    """
    Participant type

    This value set defines a set of codes that can be used to indicate how
an individual participates in an encounter.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/participant-type
    """

    translator = CodeSystemConcept(
        {
            "code": "translator",
            "definition": "A translator who is facilitating communication with the patient during the encounter.",
            "display": "Translator",
        }
    )
    """
    Translator

    A translator who is facilitating communication with the patient during the encounter.
    """

    emergency = CodeSystemConcept(
        {
            "code": "emergency",
            "definition": "A person to be contacted in case of an emergency during the encounter.",
            "display": "Emergency",
        }
    )
    """
    Emergency

    A person to be contacted in case of an emergency during the encounter.
    """

    class Meta:
        resource = _resource
