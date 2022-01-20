from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["QuestionnaireAnswerCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class QuestionnaireAnswerCodes(SNOMEDCT):
    """
    Questionnaire Answer Codes

    Example list of codes for answers to questions. (Not complete or
necessarily appropriate.)

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/questionnaire-answers
    """

    class Meta:
        resource = _resource
