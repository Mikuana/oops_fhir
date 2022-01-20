from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.questionnaire_item_uicontrol_codes import (
    QuestionnaireItemUIControlCodes as QuestionnaireItemUIControlCodes_,
)


__all__ = ["QuestionnaireItemUIControlCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class QuestionnaireItemUIControlCodes(QuestionnaireItemUIControlCodes_):
    """
    Questionnaire Item UI Control Codes

    Starter set of user interface control/display mechanisms that might be
used when rendering an item in a questionnaire.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/questionnaire-item-control
    """

    class Meta:
        resource = _resource
