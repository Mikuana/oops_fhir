from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["QuestionnaireItemUsageMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class QuestionnaireItemUsageMode:
    """
    QuestionnaireItemUsageMode

    Identifies the modes of usage of a questionnaire that should enable a
particular questionnaire item.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/questionnaire-usage-mode
    """

    capture_display = CodeSystemConcept(
        {
            "code": "capture-display",
            "definition": "Render the item regardless of usage mode.",
            "display": "Capture & Display",
        }
    )
    """
    Capture & Display

    Render the item regardless of usage mode.
    """

    capture = CodeSystemConcept(
        {
            "code": "capture",
            "definition": "Render the item only when capturing data.",
            "display": "Capture Only",
        }
    )
    """
    Capture Only

    Render the item only when capturing data.
    """

    display = CodeSystemConcept(
        {
            "code": "display",
            "definition": "Render the item only when displaying a completed form.",
            "display": "Display Only",
        }
    )
    """
    Display Only

    Render the item only when displaying a completed form.
    """

    display_non_empty = CodeSystemConcept(
        {
            "code": "display-non-empty",
            "definition": "Render the item only when displaying a completed form and the item has been answered (or has child items that have been answered).",
            "display": "Display when Answered",
        }
    )
    """
    Display when Answered

    Render the item only when displaying a completed form and the item has been answered (or has child items that have been answered).
    """

    capture_display_non_empty = CodeSystemConcept(
        {
            "code": "capture-display-non-empty",
            "definition": "Render the item when capturing data or when displaying a completed form and the item has been answered (or has child items that have been answered).",
            "display": "Capture or, if answered, Display",
        }
    )
    """
    Capture or, if answered, Display

    Render the item when capturing data or when displaying a completed form and the item has been answered (or has child items that have been answered).
    """

    class Meta:
        resource = _resource
