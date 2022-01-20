from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.questionnaire_item_usage_mode import (
    QuestionnaireItemUsageMode as QuestionnaireItemUsageMode_,
)


__all__ = ["QuestionnaireItemUsageMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class QuestionnaireItemUsageMode(QuestionnaireItemUsageMode_):
    """
    QuestionnaireItemUsageMode

    Identifies the modes of usage of a questionnaire that should enable a
particular questionnaire item.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/questionnaire-usage-mode
    """

    class Meta:
        resource = _resource
