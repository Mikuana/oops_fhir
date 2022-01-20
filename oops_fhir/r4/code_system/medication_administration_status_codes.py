from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MedicationAdministrationStatusCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MedicationAdministrationStatusCodes:
    """
    Medication administration  status  codes

    MedicationAdministration Status Codes

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/medication-admin-status
    """

    in_progress = CodeSystemConcept(
        {
            "code": "in-progress",
            "definition": "The administration has started but has not yet completed.",
            "display": "In Progress",
        }
    )
    """
    In Progress

    The administration has started but has not yet completed.
    """

    not_done = CodeSystemConcept(
        {
            "code": "not-done",
            "definition": "The administration was terminated prior to any impact on the subject (though preparatory actions may have been taken)",
            "display": "Not Done",
        }
    )
    """
    Not Done

    The administration was terminated prior to any impact on the subject (though preparatory actions may have been taken)
    """

    on_hold = CodeSystemConcept(
        {
            "code": "on-hold",
            "definition": "Actions implied by the administration have been temporarily halted, but are expected to continue later. May also be called 'suspended'.",
            "display": "On Hold",
        }
    )
    """
    On Hold

    Actions implied by the administration have been temporarily halted, but are expected to continue later. May also be called 'suspended'.
    """

    completed = CodeSystemConcept(
        {
            "code": "completed",
            "definition": "All actions that are implied by the administration have occurred.",
            "display": "Completed",
        }
    )
    """
    Completed

    All actions that are implied by the administration have occurred.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The administration was entered in error and therefore nullified.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The administration was entered in error and therefore nullified.
    """

    stopped = CodeSystemConcept(
        {
            "code": "stopped",
            "definition": "Actions implied by the administration have been permanently halted, before all of them occurred.",
            "display": "Stopped",
        }
    )
    """
    Stopped

    Actions implied by the administration have been permanently halted, before all of them occurred.
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": "The authoring system does not know which of the status values currently applies for this request. Note: This concept is not to be used for 'other' - one of the listed statuses is presumed to apply, it's just not known which one.",
            "display": "Unknown",
        }
    )
    """
    Unknown

    The authoring system does not know which of the status values currently applies for this request. Note: This concept is not to be used for 'other' - one of the listed statuses is presumed to apply, it's just not known which one.
    """

    class Meta:
        resource = _resource
