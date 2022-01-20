from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["EncounterStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class EncounterStatus:
    """
    EncounterStatus

    Current state of the encounter.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/encounter-status
    """

    planned = CodeSystemConcept(
        {
            "code": "planned",
            "definition": "The Encounter has not yet started.",
            "display": "Planned",
        }
    )
    """
    Planned

    The Encounter has not yet started.
    """

    arrived = CodeSystemConcept(
        {
            "code": "arrived",
            "definition": "The Patient is present for the encounter, however is not currently meeting with a practitioner.",
            "display": "Arrived",
        }
    )
    """
    Arrived

    The Patient is present for the encounter, however is not currently meeting with a practitioner.
    """

    triaged = CodeSystemConcept(
        {
            "code": "triaged",
            "definition": "The patient has been assessed for the priority of their treatment based on the severity of their condition.",
            "display": "Triaged",
        }
    )
    """
    Triaged

    The patient has been assessed for the priority of their treatment based on the severity of their condition.
    """

    in_progress = CodeSystemConcept(
        {
            "code": "in-progress",
            "definition": "The Encounter has begun and the patient is present / the practitioner and the patient are meeting.",
            "display": "In Progress",
        }
    )
    """
    In Progress

    The Encounter has begun and the patient is present / the practitioner and the patient are meeting.
    """

    onleave = CodeSystemConcept(
        {
            "code": "onleave",
            "definition": "The Encounter has begun, but the patient is temporarily on leave.",
            "display": "On Leave",
        }
    )
    """
    On Leave

    The Encounter has begun, but the patient is temporarily on leave.
    """

    finished = CodeSystemConcept(
        {
            "code": "finished",
            "definition": "The Encounter has ended.",
            "display": "Finished",
        }
    )
    """
    Finished

    The Encounter has ended.
    """

    cancelled = CodeSystemConcept(
        {
            "code": "cancelled",
            "definition": "The Encounter has ended before it has begun.",
            "display": "Cancelled",
        }
    )
    """
    Cancelled

    The Encounter has ended before it has begun.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "This instance should not have been part of this patient's medical record.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    This instance should not have been part of this patient's medical record.
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": 'The encounter status is unknown. Note that "unknown" is a value of last resort and every attempt should be made to provide a meaningful value other than "unknown".',
            "display": "Unknown",
        }
    )
    """
    Unknown

    The encounter status is unknown. Note that "unknown" is a value of last resort and every attempt should be made to provide a meaningful value other than "unknown".
    """

    class Meta:
        resource = _resource
