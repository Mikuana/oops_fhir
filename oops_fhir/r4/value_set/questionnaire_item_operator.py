from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.questionnaire_item_operator import (
    QuestionnaireItemOperator as QuestionnaireItemOperator_,
)


__all__ = ["QuestionnaireItemOperator"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class QuestionnaireItemOperator(QuestionnaireItemOperator_):
    """
    QuestionnaireItemOperator

    The criteria by which a question is enabled.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/questionnaire-enable-operator
    """

    class Meta:
        resource = _resource
