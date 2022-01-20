from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["QuestionnaireResponseStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class QuestionnaireResponseStatus:
    """
    QuestionnaireResponseStatus

    Lifecycle status of the questionnaire response.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/questionnaire-answers-status
    """

    in_progress = CodeSystemConcept(
        {
            "code": "in-progress",
            "definition": "This QuestionnaireResponse has been partially filled out with answers but changes or additions are still expected to be made to it.",
            "display": "In Progress",
        }
    )
    """
    In Progress

    This QuestionnaireResponse has been partially filled out with answers but changes or additions are still expected to be made to it.
    """

    completed = CodeSystemConcept(
        {
            "code": "completed",
            "definition": "This QuestionnaireResponse has been filled out with answers and the current content is regarded as definitive.",
            "display": "Completed",
        }
    )
    """
    Completed

    This QuestionnaireResponse has been filled out with answers and the current content is regarded as definitive.
    """

    amended = CodeSystemConcept(
        {
            "code": "amended",
            "definition": "This QuestionnaireResponse has been filled out with answers, then marked as complete, yet changes or additions have been made to it afterwards.",
            "display": "Amended",
        }
    )
    """
    Amended

    This QuestionnaireResponse has been filled out with answers, then marked as complete, yet changes or additions have been made to it afterwards.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "This QuestionnaireResponse was entered in error and voided.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    This QuestionnaireResponse was entered in error and voided.
    """

    stopped = CodeSystemConcept(
        {
            "code": "stopped",
            "definition": "This QuestionnaireResponse has been partially filled out with answers but has been abandoned. It is unknown whether changes or additions are expected to be made to it.",
            "display": "Stopped",
        }
    )
    """
    Stopped

    This QuestionnaireResponse has been partially filled out with answers but has been abandoned. It is unknown whether changes or additions are expected to be made to it.
    """

    class Meta:
        resource = _resource
