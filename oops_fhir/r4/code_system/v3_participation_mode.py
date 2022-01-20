from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ParticipationMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ParticipationMode:
    """
    v3 Code System ParticipationMode

     A set of codes specifying the modality by which the Entity playing the
Role is participating in the Act.  Examples:  Physically present, over
the telephone, written communication.  Rationale:  Particularly for
author (originator) participants this is used to specify whether the
information represented by the act was initially provided verbally,
(hand-)written, or electronically.  Open Issue:  There needs to be a
reexamination of the hierarchies as there seems to be some muddling
between ELECTRONIC and other concepts that involve electronic
communication that are in other hierarchies.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ParticipationMode
    """

    electronic = CodeSystemConcept(
        {
            "code": "ELECTRONIC",
            "definition": "Participation by non-human-languaged based electronic signal",
            "display": "electronic data",
        }
    )
    """
    electronic data

    Participation by non-human-languaged based electronic signal
    """

    physical = CodeSystemConcept(
        {
            "code": "PHYSICAL",
            "definition": "Participation by direct action where subject and actor are in the same location. (The participation involves more than communication.)",
            "display": "physical presence",
        }
    )
    """
    physical presence

    Participation by direct action where subject and actor are in the same location. (The participation involves more than communication.)
    """

    remote = CodeSystemConcept(
        {
            "code": "REMOTE",
            "definition": "Participation by direct action where subject and actor are in separate locations, and the actions of the actor are transmitted by electronic or mechanical means. (The participation involves more than communication.)",
            "display": "remote presence",
        }
    )
    """
    remote presence

    Participation by direct action where subject and actor are in separate locations, and the actions of the actor are transmitted by electronic or mechanical means. (The participation involves more than communication.)
    """

    verbal = CodeSystemConcept(
        {
            "code": "VERBAL",
            "concept": [
                {
                    "code": "DICTATE",
                    "definition": "Participation by pre-recorded voice.  Communication is limited to one direction (from the recorder to recipient).",
                    "display": "dictated",
                },
                {
                    "code": "FACE",
                    "definition": "Participation by voice communication where parties speak to each other directly.",
                    "display": "face-to-face",
                },
                {
                    "code": "PHONE",
                    "definition": "Participation by voice communication where the voices of the communicating parties are transported over an electronic medium",
                    "display": "telephone",
                },
                {
                    "code": "VIDEOCONF",
                    "definition": "Participation by voice and visual communication where the voices and images of the communicating parties are transported over an electronic medium",
                    "display": "videoconferencing",
                },
            ],
            "definition": "Participation by voice communication",
            "display": "verbal",
        }
    )
    """
    verbal

    Participation by voice communication
    """

    written = CodeSystemConcept(
        {
            "code": "WRITTEN",
            "concept": [
                {
                    "code": "FAXWRIT",
                    "definition": "Participation by text or diagrams printed on paper that have been transmitted over a fax device",
                    "display": "telefax",
                },
                {
                    "code": "HANDWRIT",
                    "definition": "Participation by text or diagrams printed on paper or other recording medium",
                    "display": "handwritten",
                },
                {
                    "code": "MAILWRIT",
                    "definition": "Participation by text or diagrams printed on paper transmitted physically (e.g. by courier service, postal service).",
                    "display": "mail",
                },
                {
                    "code": "ONLINEWRIT",
                    "concept": [
                        {
                            "code": "EMAILWRIT",
                            "definition": "Participation by text or diagrams transmitted over an electronic mail system.",
                            "display": "email",
                        }
                    ],
                    "definition": "Participation by text or diagrams submitted by computer network, e.g. online survey.",
                    "display": "online written",
                },
                {
                    "code": "TYPEWRIT",
                    "definition": "Participation by text or diagrams printed on paper or other recording medium where the recording was performed using a typewriter, typesetter, computer or similar mechanism.",
                    "display": "typewritten",
                },
            ],
            "definition": "Participation by human language recorded on a physical material",
            "display": "written",
        }
    )
    """
    written

    Participation by human language recorded on a physical material
    """

    class Meta:
        resource = _resource
