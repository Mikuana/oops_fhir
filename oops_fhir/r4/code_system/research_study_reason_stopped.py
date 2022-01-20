from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ResearchStudyReasonStopped"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ResearchStudyReasonStopped:
    """
    ResearchStudyReasonStopped

    Codes for why the study ended prematurely.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/research-study-reason-stopped
    """

    accrual_goal_met = CodeSystemConcept(
        {
            "code": "accrual-goal-met",
            "definition": "The study prematurely ended because the accrual goal was met.",
            "display": "Accrual Goal Met",
        }
    )
    """
    Accrual Goal Met

    The study prematurely ended because the accrual goal was met.
    """

    closed_due_to_toxicity = CodeSystemConcept(
        {
            "code": "closed-due-to-toxicity",
            "definition": "The study prematurely ended due to toxicity.",
            "display": "Closed due to toxicity",
        }
    )
    """
    Closed due to toxicity

    The study prematurely ended due to toxicity.
    """

    closed_due_to_lack_of_study_progress = CodeSystemConcept(
        {
            "code": "closed-due-to-lack-of-study-progress",
            "definition": "The study prematurely ended due to lack of study progress.",
            "display": "Closed due to lack of study progress",
        }
    )
    """
    Closed due to lack of study progress

    The study prematurely ended due to lack of study progress.
    """

    temporarily_closed_per_study_design = CodeSystemConcept(
        {
            "code": "temporarily-closed-per-study-design",
            "definition": "The study prematurely ended temporarily per study design.",
            "display": "Temporarily closed per study design",
        }
    )
    """
    Temporarily closed per study design

    The study prematurely ended temporarily per study design.
    """

    class Meta:
        resource = _resource
