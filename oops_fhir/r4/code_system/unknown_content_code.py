from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["UnknownContentCode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class UnknownContentCode:
    """
    UnknownContentCode

    A code that indicates whether an application accepts unknown elements or
extensions when reading resources.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/unknown-content-code
    """

    no = CodeSystemConcept(
        {
            "code": "no",
            "definition": "The application does not accept either unknown elements or extensions.",
            "display": "Neither Elements or Extensions",
        }
    )
    """
    Neither Elements or Extensions

    The application does not accept either unknown elements or extensions.
    """

    extensions = CodeSystemConcept(
        {
            "code": "extensions",
            "definition": "The application accepts unknown extensions, but not unknown elements.",
            "display": "Unknown Extensions",
        }
    )
    """
    Unknown Extensions

    The application accepts unknown extensions, but not unknown elements.
    """

    elements = CodeSystemConcept(
        {
            "code": "elements",
            "definition": "The application accepts unknown elements, but not unknown extensions.",
            "display": "Unknown Elements",
        }
    )
    """
    Unknown Elements

    The application accepts unknown elements, but not unknown extensions.
    """

    both = CodeSystemConcept(
        {
            "code": "both",
            "definition": "The application accepts unknown elements and extensions.",
            "display": "Unknown Elements and Extensions",
        }
    )
    """
    Unknown Elements and Extensions

    The application accepts unknown elements and extensions.
    """

    class Meta:
        resource = _resource
