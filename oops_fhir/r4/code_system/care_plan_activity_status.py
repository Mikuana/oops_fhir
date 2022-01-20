from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CarePlanActivityStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CarePlanActivityStatus:
    """
    CarePlanActivityStatus

    Codes that reflect the current state of a care plan activity within its
overall life cycle.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/care-plan-activity-status
    """

    not_started = CodeSystemConcept(
        {
            "code": "not-started",
            "definition": "Care plan activity is planned but no action has yet been taken.",
            "display": "Not Started",
        }
    )
    """
    Not Started

    Care plan activity is planned but no action has yet been taken.
    """

    scheduled = CodeSystemConcept(
        {
            "code": "scheduled",
            "definition": "Appointment or other booking has occurred but activity has not yet begun.",
            "display": "Scheduled",
        }
    )
    """
    Scheduled

    Appointment or other booking has occurred but activity has not yet begun.
    """

    in_progress = CodeSystemConcept(
        {
            "code": "in-progress",
            "definition": "Care plan activity has been started but is not yet complete.",
            "display": "In Progress",
        }
    )
    """
    In Progress

    Care plan activity has been started but is not yet complete.
    """

    on_hold = CodeSystemConcept(
        {
            "code": "on-hold",
            "definition": "Care plan activity was started but has temporarily ceased with an expectation of resumption at a future time.",
            "display": "On Hold",
        }
    )
    """
    On Hold

    Care plan activity was started but has temporarily ceased with an expectation of resumption at a future time.
    """

    completed = CodeSystemConcept(
        {
            "code": "completed",
            "definition": "Care plan activity has been completed (more or less) as planned.",
            "display": "Completed",
        }
    )
    """
    Completed

    Care plan activity has been completed (more or less) as planned.
    """

    cancelled = CodeSystemConcept(
        {
            "code": "cancelled",
            "concept": [
                {
                    "code": "stopped",
                    "definition": "The planned care plan activity has been ended prior to completion after the activity was started.",
                    "display": "Stopped",
                }
            ],
            "definition": "The planned care plan activity has been withdrawn.",
            "display": "Cancelled",
        }
    )
    """
    Cancelled

    The planned care plan activity has been withdrawn.
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": 'The current state of the care plan activity is not known.  Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, but the authoring/source system does not know which one.',
            "display": "Unknown",
        }
    )
    """
    Unknown

    The current state of the care plan activity is not known.  Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, but the authoring/source system does not know which one.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "Care plan activity was entered in error and voided.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    Care plan activity was entered in error and voided.
    """

    class Meta:
        resource = _resource
