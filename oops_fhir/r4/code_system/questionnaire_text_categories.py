from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["QuestionnaireTextCategories"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class QuestionnaireTextCategories:
    """
    Questionnaire Text Categories

    Codes defining the purpose of a Questionnaire item of type 'text'.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/questionnaire-display-category
    """

    instructions = CodeSystemConcept(
        {
            "code": "instructions",
            "definition": "The text provides guidance on how to populate or use a portion of the questionnaire (or the questionnaire as a whole).",
            "display": "Instructions",
        }
    )
    """
    Instructions

    The text provides guidance on how to populate or use a portion of the questionnaire (or the questionnaire as a whole).
    """

    security = CodeSystemConcept(
        {
            "code": "security",
            "definition": "The text provides guidance on how the information should be or will be handled from a security/confidentiality/access control perspective when completed",
            "display": "Security",
        }
    )
    """
    Security

    The text provides guidance on how the information should be or will be handled from a security/confidentiality/access control perspective when completed
    """

    help_ = CodeSystemConcept(
        {
            "code": "help",
            "definition": 'The text provides additional guidance on populating the containing item.  Help text isn\'t necessarily expected to be rendered as part of the form, but may instead be made available through fly-over, pop-up button, link to a "help" page, etc.',
            "display": "Help",
        }
    )
    """
    Help

    The text provides additional guidance on populating the containing item.  Help text isn't necessarily expected to be rendered as part of the form, but may instead be made available through fly-over, pop-up button, link to a "help" page, etc.
    """

    class Meta:
        resource = _resource
