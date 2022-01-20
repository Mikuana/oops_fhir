from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ResearchStudyStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ResearchStudyStatus:
    """
    ResearchStudyStatus

    Codes that convey the current status of the research study.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/research-study-status
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "Study is opened for accrual.",
            "display": "Active",
        }
    )
    """
    Active

    Study is opened for accrual.
    """

    administratively_completed = CodeSystemConcept(
        {
            "code": "administratively-completed",
            "definition": "Study is completed prematurely and will not resume; patients are no longer examined nor treated.",
            "display": "Administratively Completed",
        }
    )
    """
    Administratively Completed

    Study is completed prematurely and will not resume; patients are no longer examined nor treated.
    """

    approved = CodeSystemConcept(
        {
            "code": "approved",
            "definition": "Protocol is approved by the review board.",
            "display": "Approved",
        }
    )
    """
    Approved

    Protocol is approved by the review board.
    """

    closed_to_accrual = CodeSystemConcept(
        {
            "code": "closed-to-accrual",
            "definition": "Study is closed for accrual; patients can be examined and treated.",
            "display": "Closed to Accrual",
        }
    )
    """
    Closed to Accrual

    Study is closed for accrual; patients can be examined and treated.
    """

    closed_to_accrual_and_intervention = CodeSystemConcept(
        {
            "code": "closed-to-accrual-and-intervention",
            "definition": "Study is closed to accrual and intervention, i.e. the study is closed to enrollment, all study subjects have completed treatment or intervention but are still being followed according to the primary objective of the study.",
            "display": "Closed to Accrual and Intervention",
        }
    )
    """
    Closed to Accrual and Intervention

    Study is closed to accrual and intervention, i.e. the study is closed to enrollment, all study subjects have completed treatment or intervention but are still being followed according to the primary objective of the study.
    """

    completed = CodeSystemConcept(
        {
            "code": "completed",
            "definition": "Study is closed to accrual and intervention, i.e. the study is closed to enrollment, all study subjects have completed treatment\nor intervention but are still being followed according to the primary objective of the study.",
            "display": "Completed",
        }
    )
    """
    Completed

    Study is closed to accrual and intervention, i.e. the study is closed to enrollment, all study subjects have completed treatment
or intervention but are still being followed according to the primary objective of the study.
    """

    disapproved = CodeSystemConcept(
        {
            "code": "disapproved",
            "definition": "Protocol was disapproved by the review board.",
            "display": "Disapproved",
        }
    )
    """
    Disapproved

    Protocol was disapproved by the review board.
    """

    in_review = CodeSystemConcept(
        {
            "code": "in-review",
            "definition": "Protocol is submitted to the review board for approval.",
            "display": "In Review",
        }
    )
    """
    In Review

    Protocol is submitted to the review board for approval.
    """

    temporarily_closed_to_accrual = CodeSystemConcept(
        {
            "code": "temporarily-closed-to-accrual",
            "definition": "Study is temporarily closed for accrual; can be potentially resumed in the future; patients can be examined and treated.",
            "display": "Temporarily Closed to Accrual",
        }
    )
    """
    Temporarily Closed to Accrual

    Study is temporarily closed for accrual; can be potentially resumed in the future; patients can be examined and treated.
    """

    temporarily_closed_to_accrual_and_intervention = CodeSystemConcept(
        {
            "code": "temporarily-closed-to-accrual-and-intervention",
            "definition": "Study is temporarily closed for accrual and intervention and potentially can be resumed in the future.",
            "display": "Temporarily Closed to Accrual and Intervention",
        }
    )
    """
    Temporarily Closed to Accrual and Intervention

    Study is temporarily closed for accrual and intervention and potentially can be resumed in the future.
    """

    withdrawn = CodeSystemConcept(
        {
            "code": "withdrawn",
            "definition": "Protocol was withdrawn by the lead organization.",
            "display": "Withdrawn",
        }
    )
    """
    Withdrawn

    Protocol was withdrawn by the lead organization.
    """

    class Meta:
        resource = _resource
