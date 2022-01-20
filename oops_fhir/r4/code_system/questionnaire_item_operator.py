from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["QuestionnaireItemOperator"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class QuestionnaireItemOperator:
    """
    QuestionnaireItemOperator

    The criteria by which a question is enabled.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/questionnaire-enable-operator
    """

    exists = CodeSystemConcept(
        {
            "code": "exists",
            "definition": "True if whether an answer exists is equal to the enableWhen answer (which must be a boolean).",
            "display": "Exists",
        }
    )
    """
    Exists

    True if whether an answer exists is equal to the enableWhen answer (which must be a boolean).
    """

    equals_to = CodeSystemConcept(
        {
            "code": "=",
            "definition": "True if whether at least one answer has a value that is equal to the enableWhen answer.",
            "display": "Equals",
        }
    )
    """
    Equals

    True if whether at least one answer has a value that is equal to the enableWhen answer.
    """

    exclamation_mark = CodeSystemConcept(
        {
            "code": "!=",
            "definition": "True if whether at least no answer has a value that is equal to the enableWhen answer.",
            "display": "Not Equals",
        }
    )
    """
    Not Equals

    True if whether at least no answer has a value that is equal to the enableWhen answer.
    """

    greater_than = CodeSystemConcept(
        {
            "code": ">",
            "definition": "True if whether at least no answer has a value that is greater than the enableWhen answer.",
            "display": "Greater Than",
        }
    )
    """
    Greater Than

    True if whether at least no answer has a value that is greater than the enableWhen answer.
    """

    less_than = CodeSystemConcept(
        {
            "code": "<",
            "definition": "True if whether at least no answer has a value that is less than the enableWhen answer.",
            "display": "Less Than",
        }
    )
    """
    Less Than

    True if whether at least no answer has a value that is less than the enableWhen answer.
    """

    greater_than = CodeSystemConcept(
        {
            "code": ">=",
            "definition": "True if whether at least no answer has a value that is greater or equal to the enableWhen answer.",
            "display": "Greater or Equals",
        }
    )
    """
    Greater or Equals

    True if whether at least no answer has a value that is greater or equal to the enableWhen answer.
    """

    less_than = CodeSystemConcept(
        {
            "code": "<=",
            "definition": "True if whether at least no answer has a value that is less or equal to the enableWhen answer.",
            "display": "Less or Equals",
        }
    )
    """
    Less or Equals

    True if whether at least no answer has a value that is less or equal to the enableWhen answer.
    """

    class Meta:
        resource = _resource
