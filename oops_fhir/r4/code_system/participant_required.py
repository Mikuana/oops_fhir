from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ParticipantRequired"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ParticipantRequired:
    """
    ParticipantRequired

    Is the Participant required to attend the appointment.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/participantrequired
    """

    required = CodeSystemConcept(
        {
            "code": "required",
            "definition": "The participant is required to attend the appointment.",
            "display": "Required",
        }
    )
    """
    Required

    The participant is required to attend the appointment.
    """

    optional = CodeSystemConcept(
        {
            "code": "optional",
            "definition": "The participant may optionally attend the appointment.",
            "display": "Optional",
        }
    )
    """
    Optional

    The participant may optionally attend the appointment.
    """

    information_only = CodeSystemConcept(
        {
            "code": "information-only",
            "definition": "The participant is excluded from the appointment, and might not be informed of the appointment taking place. (Appointment is about them, not for them - such as 2 doctors discussing results about a patient's test).",
            "display": "Information Only",
        }
    )
    """
    Information Only

    The participant is excluded from the appointment, and might not be informed of the appointment taking place. (Appointment is about them, not for them - such as 2 doctors discussing results about a patient's test).
    """

    class Meta:
        resource = _resource
