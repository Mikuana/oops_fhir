from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ChoiceListOrientation"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ChoiceListOrientation:
    """
    ChoiceListOrientation

    Direction in which lists of possible answers should be displayed.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/choice-list-orientation
    """

    horizontal = CodeSystemConcept(
        {
            "code": "horizontal",
            "definition": "List choices along the horizontal axis.",
            "display": "Horizontal",
        }
    )
    """
    Horizontal

    List choices along the horizontal axis.
    """

    vertical = CodeSystemConcept(
        {
            "code": "vertical",
            "definition": "List choices down the vertical axis.",
            "display": "Vertical",
        }
    )
    """
    Vertical

    List choices down the vertical axis.
    """

    class Meta:
        resource = _resource
