from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SlotStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SlotStatus:
    """
    SlotStatus

    The free/busy status of the slot.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/slotstatus
    """

    busy = CodeSystemConcept(
        {
            "code": "busy",
            "definition": "Indicates that the time interval is busy because one  or more events have been scheduled for that interval.",
            "display": "Busy",
        }
    )
    """
    Busy

    Indicates that the time interval is busy because one  or more events have been scheduled for that interval.
    """

    free = CodeSystemConcept(
        {
            "code": "free",
            "definition": "Indicates that the time interval is free for scheduling.",
            "display": "Free",
        }
    )
    """
    Free

    Indicates that the time interval is free for scheduling.
    """

    busy_unavailable = CodeSystemConcept(
        {
            "code": "busy-unavailable",
            "definition": "Indicates that the time interval is busy and that the interval cannot be scheduled.",
            "display": "Busy (Unavailable)",
        }
    )
    """
    Busy (Unavailable)

    Indicates that the time interval is busy and that the interval cannot be scheduled.
    """

    busy_tentative = CodeSystemConcept(
        {
            "code": "busy-tentative",
            "definition": "Indicates that the time interval is busy because one or more events have been tentatively scheduled for that interval.",
            "display": "Busy (Tentative)",
        }
    )
    """
    Busy (Tentative)

    Indicates that the time interval is busy because one or more events have been tentatively scheduled for that interval.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "This instance should not have been part of this patient's medical record.",
            "display": "Entered in error",
        }
    )
    """
    Entered in error

    This instance should not have been part of this patient's medical record.
    """

    class Meta:
        resource = _resource
