from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["QuestionnaireItemType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class QuestionnaireItemType:
    """
    QuestionnaireItemType

    Distinguishes groups from questions and display text and indicates data
type for questions.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/item-type
    """

    group = CodeSystemConcept(
        {
            "code": "group",
            "definition": "An item with no direct answer but should have at least one child item.",
            "display": "Group",
        }
    )
    """
    Group

    An item with no direct answer but should have at least one child item.
    """

    display = CodeSystemConcept(
        {
            "code": "display",
            "definition": "Text for display that will not capture an answer or have child items.",
            "display": "Display",
        }
    )
    """
    Display

    Text for display that will not capture an answer or have child items.
    """

    question = CodeSystemConcept(
        {
            "code": "question",
            "concept": [
                {
                    "code": "boolean",
                    "definition": "Question with a yes/no answer (valueBoolean).",
                    "display": "Boolean",
                },
                {
                    "code": "decimal",
                    "definition": "Question with is a real number answer (valueDecimal).",
                    "display": "Decimal",
                },
                {
                    "code": "integer",
                    "definition": "Question with an integer answer (valueInteger).",
                    "display": "Integer",
                },
                {
                    "code": "date",
                    "definition": "Question with a date answer (valueDate).",
                    "display": "Date",
                },
                {
                    "code": "dateTime",
                    "definition": "Question with a date and time answer (valueDateTime).",
                    "display": "Date Time",
                },
                {
                    "code": "time",
                    "definition": "Question with a time (hour:minute:second) answer independent of date. (valueTime).",
                    "display": "Time",
                },
                {
                    "code": "string",
                    "definition": "Question with a short (few words to short sentence) free-text entry answer (valueString).",
                    "display": "String",
                },
                {
                    "code": "text",
                    "definition": "Question with a long (potentially multi-paragraph) free-text entry answer (valueString).",
                    "display": "Text",
                },
                {
                    "code": "url",
                    "definition": "Question with a URL (website, FTP site, etc.) answer (valueUri).",
                    "display": "Url",
                },
                {
                    "code": "choice",
                    "definition": "Question with a Coding drawn from a list of possible answers (specified in either the answerOption property, or via the valueset referenced in the answerValueSet property) as an answer (valueCoding).",
                    "display": "Choice",
                },
                {
                    "code": "open-choice",
                    "definition": "Answer is a Coding drawn from a list of possible answers (as with the choice type) or a free-text entry in a string (valueCoding or valueString).",
                    "display": "Open Choice",
                },
                {
                    "code": "attachment",
                    "definition": "Question with binary content such as an image, PDF, etc. as an answer (valueAttachment).",
                    "display": "Attachment",
                },
                {
                    "code": "reference",
                    "definition": "Question with a reference to another resource (practitioner, organization, etc.) as an answer (valueReference).",
                    "display": "Reference",
                },
                {
                    "code": "quantity",
                    "definition": "Question with a combination of a numeric value and unit, potentially with a comparator (<, >, etc.) as an answer. (valueQuantity) There is an extension 'http://hl7.org/fhir/StructureDefinition/questionnaire-unit' that can be used to define what unit should be captured (or the unit that has a ucum conversion from the provided unit).",
                    "display": "Quantity",
                },
            ],
            "definition": "An item that defines a specific answer to be captured, and which may have child items. (the answer provided in the QuestionnaireResponse should be of the defined datatype).",
            "display": "Question",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Question

    An item that defines a specific answer to be captured, and which may have child items. (the answer provided in the QuestionnaireResponse should be of the defined datatype).
    """

    class Meta:
        resource = _resource
