from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["TaskStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class TaskStatus:
    """
    TaskStatus

    The current status of the task.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/task-status
    """

    draft = CodeSystemConcept(
        {
            "code": "draft",
            "definition": "The task is not yet ready to be acted upon.",
            "display": "Draft",
        }
    )
    """
    Draft

    The task is not yet ready to be acted upon.
    """

    requested = CodeSystemConcept(
        {
            "code": "requested",
            "definition": "The task is ready to be acted upon and action is sought.",
            "display": "Requested",
        }
    )
    """
    Requested

    The task is ready to be acted upon and action is sought.
    """

    received = CodeSystemConcept(
        {
            "code": "received",
            "definition": "A potential performer has claimed ownership of the task and is evaluating whether to perform it.",
            "display": "Received",
        }
    )
    """
    Received

    A potential performer has claimed ownership of the task and is evaluating whether to perform it.
    """

    accepted = CodeSystemConcept(
        {
            "code": "accepted",
            "definition": "The potential performer has agreed to execute the task but has not yet started work.",
            "display": "Accepted",
        }
    )
    """
    Accepted

    The potential performer has agreed to execute the task but has not yet started work.
    """

    rejected = CodeSystemConcept(
        {
            "code": "rejected",
            "definition": "The potential performer who claimed ownership of the task has decided not to execute it prior to performing any action.",
            "display": "Rejected",
        }
    )
    """
    Rejected

    The potential performer who claimed ownership of the task has decided not to execute it prior to performing any action.
    """

    ready = CodeSystemConcept(
        {
            "code": "ready",
            "definition": "The task is ready to be performed, but no action has yet been taken.  Used in place of requested/received/accepted/rejected when request assignment and acceptance is a given.",
            "display": "Ready",
        }
    )
    """
    Ready

    The task is ready to be performed, but no action has yet been taken.  Used in place of requested/received/accepted/rejected when request assignment and acceptance is a given.
    """

    cancelled = CodeSystemConcept(
        {
            "code": "cancelled",
            "definition": "The task was not completed.",
            "display": "Cancelled",
        }
    )
    """
    Cancelled

    The task was not completed.
    """

    in_progress = CodeSystemConcept(
        {
            "code": "in-progress",
            "definition": "The task has been started but is not yet complete.",
            "display": "In Progress",
        }
    )
    """
    In Progress

    The task has been started but is not yet complete.
    """

    on_hold = CodeSystemConcept(
        {
            "code": "on-hold",
            "definition": "The task has been started but work has been paused.",
            "display": "On Hold",
        }
    )
    """
    On Hold

    The task has been started but work has been paused.
    """

    failed = CodeSystemConcept(
        {
            "code": "failed",
            "definition": "The task was attempted but could not be completed due to some error.",
            "display": "Failed",
        }
    )
    """
    Failed

    The task was attempted but could not be completed due to some error.
    """

    completed = CodeSystemConcept(
        {
            "code": "completed",
            "definition": "The task has been completed.",
            "display": "Completed",
        }
    )
    """
    Completed

    The task has been completed.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The task should never have existed and is retained only because of the possibility it may have used.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The task should never have existed and is retained only because of the possibility it may have used.
    """

    class Meta:
        resource = _resource
