from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["GoalStatusReason"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class GoalStatusReason:
    """
    Goal status reason

    Example codes indicating the reason for a current status.  Note that
these are in no way complete and might not even be appropriate for some
uses.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/goal-status-reason
    """

    surgery = CodeSystemConcept(
        {
            "code": "surgery",
            "definition": "Goal suspended or ended because of a surgical procedure.",
            "display": "Surgery",
        }
    )
    """
    Surgery

    Goal suspended or ended because of a surgical procedure.
    """

    life_event = CodeSystemConcept(
        {
            "code": "life-event",
            "definition": "Goal suspended or ended because of a significant life event (marital change, bereavement, etc.).",
            "display": "Life Event",
        }
    )
    """
    Life Event

    Goal suspended or ended because of a significant life event (marital change, bereavement, etc.).
    """

    replaced = CodeSystemConcept(
        {
            "code": "replaced",
            "definition": "Goal has been superseded by a new goal.",
            "display": "Replaced",
        }
    )
    """
    Replaced

    Goal has been superseded by a new goal.
    """

    patient_request = CodeSystemConcept(
        {
            "code": "patient-request",
            "definition": "Patient wishes the goal to be set aside, at least temporarily.",
            "display": "Patient Request",
        }
    )
    """
    Patient Request

    Patient wishes the goal to be set aside, at least temporarily.
    """

    temp_not_attainable = CodeSystemConcept(
        {
            "code": "temp-not-attainable",
            "definition": "Goal cannot be reached temporarily.",
            "display": "Goal Not Attainable Temporarily",
        }
    )
    """
    Goal Not Attainable Temporarily

    Goal cannot be reached temporarily.
    """

    permanent_not_attainable = CodeSystemConcept(
        {
            "code": "permanent-not-attainable",
            "definition": "Goal cannot be reached permanently.",
            "display": "Goal Not Attainable Permanently",
        }
    )
    """
    Goal Not Attainable Permanently

    Goal cannot be reached permanently.
    """

    financial_barrier = CodeSystemConcept(
        {
            "code": "financial-barrier",
            "definition": "Goal cannot be reached due to financial barrier or reason.",
            "display": "Financial Reason",
        }
    )
    """
    Financial Reason

    Goal cannot be reached due to financial barrier or reason.
    """

    lack_of_transportation = CodeSystemConcept(
        {
            "code": "lack-of-transportation",
            "definition": "Goal cannot be reached due to a lack of transportation.",
            "display": "Lack Of Transportation",
        }
    )
    """
    Lack Of Transportation

    Goal cannot be reached due to a lack of transportation.
    """

    lack_of_social_support = CodeSystemConcept(
        {
            "code": "lack-of-social-support",
            "definition": "Goal cannot be reached due to a lack of social support.",
            "display": "Lack Of Social Support",
        }
    )
    """
    Lack Of Social Support

    Goal cannot be reached due to a lack of social support.
    """

    class Meta:
        resource = _resource
