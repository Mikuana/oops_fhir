from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["EventStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class EventStatus:
    """
    EventStatus

    Codes identifying the lifecycle stage of an event.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/event-status
    """

    preparation = CodeSystemConcept(
        {
            "code": "preparation",
            "definition": "The core event has not started yet, but some staging activities have begun (e.g. surgical suite preparation).  Preparation stages may be tracked for billing purposes.",
            "display": "Preparation",
        }
    )
    """
    Preparation

    The core event has not started yet, but some staging activities have begun (e.g. surgical suite preparation).  Preparation stages may be tracked for billing purposes.
    """

    in_progress = CodeSystemConcept(
        {
            "code": "in-progress",
            "definition": "The event is currently occurring.",
            "display": "In Progress",
        }
    )
    """
    In Progress

    The event is currently occurring.
    """

    not_done = CodeSystemConcept(
        {
            "code": "not-done",
            "definition": "The event was terminated prior to any activity beyond preparation.  I.e. The 'main' activity has not yet begun.  The boundary between preparatory and the 'main' activity is context-specific.",
            "display": "Not Done",
        }
    )
    """
    Not Done

    The event was terminated prior to any activity beyond preparation.  I.e. The 'main' activity has not yet begun.  The boundary between preparatory and the 'main' activity is context-specific.
    """

    on_hold = CodeSystemConcept(
        {
            "code": "on-hold",
            "definition": "The event has been temporarily stopped but is expected to resume in the future.",
            "display": "On Hold",
        }
    )
    """
    On Hold

    The event has been temporarily stopped but is expected to resume in the future.
    """

    stopped = CodeSystemConcept(
        {
            "code": "stopped",
            "definition": "The event was terminated prior to the full completion of the intended activity but after at least some of the 'main' activity (beyond preparation) has occurred.",
            "display": "Stopped",
        }
    )
    """
    Stopped

    The event was terminated prior to the full completion of the intended activity but after at least some of the 'main' activity (beyond preparation) has occurred.
    """

    completed = CodeSystemConcept(
        {
            "code": "completed",
            "definition": "The event has now concluded.",
            "display": "Completed",
        }
    )
    """
    Completed

    The event has now concluded.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": 'This electronic record should never have existed, though it is possible that real-world decisions were based on it.  (If real-world activity has occurred, the status should be "stopped" rather than "entered-in-error".).',
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    This electronic record should never have existed, though it is possible that real-world decisions were based on it.  (If real-world activity has occurred, the status should be "stopped" rather than "entered-in-error".).
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": 'The authoring/source system does not know which of the status values currently applies for this event.  Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply,  but the authoring/source system does not know which.',
            "display": "Unknown",
        }
    )
    """
    Unknown

    The authoring/source system does not know which of the status values currently applies for this event.  Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply,  but the authoring/source system does not know which.
    """

    class Meta:
        resource = _resource
