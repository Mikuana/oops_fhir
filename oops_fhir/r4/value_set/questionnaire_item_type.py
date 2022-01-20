from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.questionnaire_item_type import (
    QuestionnaireItemType as QuestionnaireItemType_,
)


__all__ = ["QuestionnaireItemType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class QuestionnaireItemType(QuestionnaireItemType_):
    """
    QuestionnaireItemType

    Distinguishes groups from questions and display text and indicates data
type for questions.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/item-type
    """

    class Meta:
        resource = _resource
