from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["QuestionnaireItemUIControlCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class QuestionnaireItemUIControlCodes:
    """
    Questionnaire Item UI Control Codes

    Starter set of user interface control/display mechanisms that might be
used when rendering an item in a questionnaire.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/questionnaire-item-control
    """

    group = CodeSystemConcept(
        {
            "code": "group",
            "concept": [
                {
                    "code": "list",
                    "definition": "Questions within the group should be listed sequentially",
                    "display": "List",
                },
                {
                    "code": "table",
                    "definition": "Questions within the group are rows in the table with possible answers as columns.  Used for 'choice' questions.",
                    "display": "Vertical Answer Table",
                },
                {
                    "code": "htable",
                    "definition": "Questions within the group are columns in the table with possible answers as rows.  Used for 'choice' questions.",
                    "display": "Horizontal Answer Table",
                },
                {
                    "code": "gtable",
                    "definition": "Questions within the group are columns in the table with each group repetition as a row.  Used for single-answer questions.",
                    "display": "Group Table",
                },
                {
                    "code": "atable",
                    "definition": "This table has one row - for the question.  Permitted answers are columns.  Used for choice questions.",
                    "display": "Answer Table",
                },
                {
                    "code": "header",
                    "definition": "The group is to be continuously visible at the top of the questionnaire",
                    "display": "Header",
                },
                {
                    "code": "footer",
                    "definition": "The group is to be continuously visible at the bottom of the questionnaire",
                    "display": "Footer",
                },
            ],
            "definition": "UI controls relevant to organizing groups of questions",
            "property": [{"code": "abstract", "valueBoolean": True}],
        }
    )
    """
    None

    UI controls relevant to organizing groups of questions
    """

    text = CodeSystemConcept(
        {
            "code": "text",
            "concept": [
                {
                    "code": "inline",
                    "definition": "Text is displayed as a paragraph in a sequential position between sibling items (default behavior)",
                    "display": "In-line",
                },
                {
                    "code": "prompt",
                    "definition": "Text is displayed immediately below or within the answer-entry area of the containing question item (typically as a guide for what to enter)",
                    "display": "Prompt",
                },
                {
                    "code": "unit",
                    "definition": "Text is displayed adjacent (horizontally or vertically) to the answer space for the parent question, typically to indicate a unit of measure",
                    "display": "Unit",
                },
                {
                    "code": "lower",
                    "definition": "Text is displayed to the left of the set of answer choices or a scaling control for the parent question item to indicate the meaning of the 'lower' bound.  E.g. 'Strongly disagree'",
                    "display": "Lower-bound",
                },
                {
                    "code": "upper",
                    "definition": "Text is displayed to the right of the set of answer choices or a scaling control for the parent question item to indicate the meaning of the 'upper' bound.  E.g. 'Strongly agree'",
                    "display": "Upper-bound",
                },
                {
                    "code": "flyover",
                    "definition": "Text is temporarily visible over top of an item if the mouse is positioned over top of the text for the containing item",
                    "display": "Fly-over",
                },
                {
                    "code": "help",
                    "definition": "Text is displayed in a dialog box or similar control if invoked by pushing a button or some other UI-appropriate action to request 'help' for a question, group or the questionnaire as a whole (depending what the text is nested within)",
                    "display": "Help-Button",
                },
            ],
            "definition": "UI controls relevant to rendering questionnaire text items",
            "property": [{"code": "abstract", "valueBoolean": True}],
        }
    )
    """
    None

    UI controls relevant to rendering questionnaire text items
    """

    question = CodeSystemConcept(
        {
            "code": "question",
            "concept": [
                {
                    "code": "autocomplete",
                    "definition": "A control which provides a list of potential matches based on text entered into a control.  Used for large choice sets where text-matching is an appropriate discovery mechanism.",
                    "display": "Auto-complete",
                },
                {
                    "code": "drop-down",
                    "definition": "A control where an item (or multiple items) can be selected from a list that is only displayed when the user is editing the field.",
                    "display": "Drop down",
                },
                {
                    "code": "check-box",
                    "definition": "A control where choices are listed with a box beside them.  The box can be toggled to select or de-select a given choice.  Multiple selections may be possible.",
                    "display": "Check-box",
                },
                {
                    "code": "lookup",
                    "definition": "A control where editing an item spawns a separate dialog box or screen permitting a user to navigate, filter or otherwise discover an appropriate match.  Useful for large choice sets where text matching is not an appropriate discovery mechanism.  Such screens must generally be tuned for the specific choice list structure.",
                    "display": "Lookup",
                },
                {
                    "code": "radio-button",
                    "definition": "A control where choices are listed with a button beside them.  The button can be toggled to select or de-select a given choice.  Selecting one item deselects all others.",
                    "display": "Radio Button",
                },
                {
                    "code": "slider",
                    "definition": "A control where an axis is displayed between the high and low values and the control can be visually manipulated to select a value anywhere on the axis.",
                    "display": "Slider",
                },
                {
                    "code": "spinner",
                    "definition": "A control where a list of numeric or other ordered values can be scrolled through via arrows.",
                    "display": "Spinner",
                },
                {
                    "code": "text-box",
                    "definition": "A control where a user can type in their answer freely.",
                    "display": "Text Box",
                },
            ],
            "definition": "UI controls relevant to capturing question data",
            "property": [{"code": "abstract", "valueBoolean": True}],
        }
    )
    """
    None

    UI controls relevant to capturing question data
    """

    class Meta:
        resource = _resource
