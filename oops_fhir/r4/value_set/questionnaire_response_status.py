from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.questionnaire_response_status import (
    QuestionnaireResponseStatus as QuestionnaireResponseStatus_,
)


__all__ = ["QuestionnaireResponseStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class QuestionnaireResponseStatus(QuestionnaireResponseStatus_):
    """
    QuestionnaireResponseStatus

    Lifecycle status of the questionnaire response.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/questionnaire-answers-status
    """

    class Meta:
        resource = _resource
