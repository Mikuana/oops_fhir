from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["QuestionnaireQuestionCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class QuestionnaireQuestionCodes(ValueSet):
    """
    Questionnaire Question Codes

    Example list of codes for questions and groups of questions. (Not
necessarily complete or appropriate.)

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/questionnaire-questions
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
