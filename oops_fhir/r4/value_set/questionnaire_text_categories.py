from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.questionnaire_text_categories import (
    QuestionnaireTextCategories as QuestionnaireTextCategories_,
)


__all__ = ["QuestionnaireTextCategories"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class QuestionnaireTextCategories(QuestionnaireTextCategories_):
    """
    Questionnaire Text Categories

    Codes defining the purpose of a Questionnaire item of type 'text'.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/questionnaire-display-category
    """

    class Meta:
        resource = _resource
