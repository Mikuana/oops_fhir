from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ParticipationStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ParticipationStatus:
    """
    ParticipationStatus

    The Participation status of an appointment.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/participationstatus
    """

    accepted = CodeSystemConcept(
        {
            "code": "accepted",
            "definition": "The participant has accepted the appointment.",
            "display": "Accepted",
        }
    )
    """
    Accepted

    The participant has accepted the appointment.
    """

    declined = CodeSystemConcept(
        {
            "code": "declined",
            "definition": "The participant has declined the appointment and will not participate in the appointment.",
            "display": "Declined",
        }
    )
    """
    Declined

    The participant has declined the appointment and will not participate in the appointment.
    """

    tentative = CodeSystemConcept(
        {
            "code": "tentative",
            "definition": "The participant has  tentatively accepted the appointment. This could be automatically created by a system and requires further processing before it can be accepted. There is no commitment that attendance will occur.",
            "display": "Tentative",
        }
    )
    """
    Tentative

    The participant has  tentatively accepted the appointment. This could be automatically created by a system and requires further processing before it can be accepted. There is no commitment that attendance will occur.
    """

    needs_action = CodeSystemConcept(
        {
            "code": "needs-action",
            "definition": "The participant needs to indicate if they accept the appointment by changing this status to one of the other statuses.",
            "display": "Needs Action",
        }
    )
    """
    Needs Action

    The participant needs to indicate if they accept the appointment by changing this status to one of the other statuses.
    """

    class Meta:
        resource = _resource
