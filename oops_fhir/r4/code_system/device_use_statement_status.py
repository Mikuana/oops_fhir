from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DeviceUseStatementStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DeviceUseStatementStatus:
    """
    DeviceUseStatementStatus

    A coded concept indicating the current status of the Device Usage.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/device-statement-status
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "The device is still being used.",
            "display": "Active",
        }
    )
    """
    Active

    The device is still being used.
    """

    completed = CodeSystemConcept(
        {
            "code": "completed",
            "definition": "The device is no longer being used.",
            "display": "Completed",
        }
    )
    """
    Completed

    The device is no longer being used.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The statement was recorded incorrectly.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The statement was recorded incorrectly.
    """

    intended = CodeSystemConcept(
        {
            "code": "intended",
            "definition": "The device may be used at some time in the future.",
            "display": "Intended",
        }
    )
    """
    Intended

    The device may be used at some time in the future.
    """

    stopped = CodeSystemConcept(
        {
            "code": "stopped",
            "definition": "Actions implied by the statement have been permanently halted, before all of them occurred.",
            "display": "Stopped",
        }
    )
    """
    Stopped

    Actions implied by the statement have been permanently halted, before all of them occurred.
    """

    on_hold = CodeSystemConcept(
        {
            "code": "on-hold",
            "definition": 'Actions implied by the statement have been temporarily halted, but are expected to continue later. May also be called "suspended".',
            "display": "On Hold",
        }
    )
    """
    On Hold

    Actions implied by the statement have been temporarily halted, but are expected to continue later. May also be called "suspended".
    """

    class Meta:
        resource = _resource
