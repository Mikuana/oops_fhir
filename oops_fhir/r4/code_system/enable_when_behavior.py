from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["EnableWhenBehavior"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class EnableWhenBehavior:
    """
    EnableWhenBehavior

    Controls how multiple enableWhen values are interpreted -  whether all
or any must be true.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/questionnaire-enable-behavior
    """

    all_ = CodeSystemConcept(
        {
            "code": "all",
            "definition": "Enable the question when all the enableWhen criteria are satisfied.",
            "display": "All",
        }
    )
    """
    All

    Enable the question when all the enableWhen criteria are satisfied.
    """

    any_ = CodeSystemConcept(
        {
            "code": "any",
            "definition": "Enable the question when any of the enableWhen criteria are satisfied.",
            "display": "Any",
        }
    )
    """
    Any

    Enable the question when any of the enableWhen criteria are satisfied.
    """

    class Meta:
        resource = _resource
