from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["EventTiming"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class EventTiming:
    """
    EventTiming

    Real world event relating to the schedule.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/event-timing
    """

    morn = CodeSystemConcept(
        {
            "code": "MORN",
            "definition": "Event occurs during the morning. The exact time is unspecified and established by institution convention or patient interpretation.",
            "display": "Morning",
        }
    )
    """
    Morning

    Event occurs during the morning. The exact time is unspecified and established by institution convention or patient interpretation.
    """

    morn_early = CodeSystemConcept(
        {
            "code": "MORN.early",
            "definition": "Event occurs during the early morning. The exact time is unspecified and established by institution convention or patient interpretation.",
            "display": "Early Morning",
        }
    )
    """
    Early Morning

    Event occurs during the early morning. The exact time is unspecified and established by institution convention or patient interpretation.
    """

    morn_late = CodeSystemConcept(
        {
            "code": "MORN.late",
            "definition": "Event occurs during the late morning. The exact time is unspecified and established by institution convention or patient interpretation.",
            "display": "Late Morning",
        }
    )
    """
    Late Morning

    Event occurs during the late morning. The exact time is unspecified and established by institution convention or patient interpretation.
    """

    noon = CodeSystemConcept(
        {
            "code": "NOON",
            "definition": "Event occurs around 12:00pm. The exact time is unspecified and established by institution convention or patient interpretation.",
            "display": "Noon",
        }
    )
    """
    Noon

    Event occurs around 12:00pm. The exact time is unspecified and established by institution convention or patient interpretation.
    """

    aft = CodeSystemConcept(
        {
            "code": "AFT",
            "definition": "Event occurs during the afternoon. The exact time is unspecified and established by institution convention or patient interpretation.",
            "display": "Afternoon",
        }
    )
    """
    Afternoon

    Event occurs during the afternoon. The exact time is unspecified and established by institution convention or patient interpretation.
    """

    aft_early = CodeSystemConcept(
        {
            "code": "AFT.early",
            "definition": "Event occurs during the early afternoon. The exact time is unspecified and established by institution convention or patient interpretation.",
            "display": "Early Afternoon",
        }
    )
    """
    Early Afternoon

    Event occurs during the early afternoon. The exact time is unspecified and established by institution convention or patient interpretation.
    """

    aft_late = CodeSystemConcept(
        {
            "code": "AFT.late",
            "definition": "Event occurs during the late afternoon. The exact time is unspecified and established by institution convention or patient interpretation.",
            "display": "Late Afternoon",
        }
    )
    """
    Late Afternoon

    Event occurs during the late afternoon. The exact time is unspecified and established by institution convention or patient interpretation.
    """

    eve = CodeSystemConcept(
        {
            "code": "EVE",
            "definition": "Event occurs during the evening. The exact time is unspecified and established by institution convention or patient interpretation.",
            "display": "Evening",
        }
    )
    """
    Evening

    Event occurs during the evening. The exact time is unspecified and established by institution convention or patient interpretation.
    """

    eve_early = CodeSystemConcept(
        {
            "code": "EVE.early",
            "definition": "Event occurs during the early evening. The exact time is unspecified and established by institution convention or patient interpretation.",
            "display": "Early Evening",
        }
    )
    """
    Early Evening

    Event occurs during the early evening. The exact time is unspecified and established by institution convention or patient interpretation.
    """

    eve_late = CodeSystemConcept(
        {
            "code": "EVE.late",
            "definition": "Event occurs during the late evening. The exact time is unspecified and established by institution convention or patient interpretation.",
            "display": "Late Evening",
        }
    )
    """
    Late Evening

    Event occurs during the late evening. The exact time is unspecified and established by institution convention or patient interpretation.
    """

    night = CodeSystemConcept(
        {
            "code": "NIGHT",
            "definition": "Event occurs during the night. The exact time is unspecified and established by institution convention or patient interpretation.",
            "display": "Night",
        }
    )
    """
    Night

    Event occurs during the night. The exact time is unspecified and established by institution convention or patient interpretation.
    """

    phs = CodeSystemConcept(
        {
            "code": "PHS",
            "definition": "Event occurs [offset] after subject goes to sleep. The exact time is unspecified and established by institution convention or patient interpretation.",
            "display": "After Sleep",
        }
    )
    """
    After Sleep

    Event occurs [offset] after subject goes to sleep. The exact time is unspecified and established by institution convention or patient interpretation.
    """

    class Meta:
        resource = _resource
