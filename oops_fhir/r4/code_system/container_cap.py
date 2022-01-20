from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContainerCap"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContainerCap:
    """
    ContainerCap

    Color of the container cap.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/container-cap
    """

    red = CodeSystemConcept(
        {"code": "red", "definition": "red cap.", "display": "red cap"}
    )
    """
    red cap

    red cap.
    """

    yellow = CodeSystemConcept(
        {"code": "yellow", "definition": "yellow cap.", "display": "yellow cap"}
    )
    """
    yellow cap

    yellow cap.
    """

    dark_yellow = CodeSystemConcept(
        {
            "code": "dark-yellow",
            "definition": "dark yellow cap.",
            "display": "dark yellow cap",
        }
    )
    """
    dark yellow cap

    dark yellow cap.
    """

    grey = CodeSystemConcept(
        {"code": "grey", "definition": "grey cap.", "display": "grey cap"}
    )
    """
    grey cap

    grey cap.
    """

    light_blue = CodeSystemConcept(
        {
            "code": "light-blue",
            "definition": "light blue cap.",
            "display": "light blue cap",
        }
    )
    """
    light blue cap

    light blue cap.
    """

    black = CodeSystemConcept(
        {"code": "black", "definition": "black cap.", "display": "black cap"}
    )
    """
    black cap

    black cap.
    """

    green = CodeSystemConcept(
        {"code": "green", "definition": "green cap.", "display": "green cap"}
    )
    """
    green cap

    green cap.
    """

    light_green = CodeSystemConcept(
        {
            "code": "light-green",
            "definition": "light green cap.",
            "display": "light green cap",
        }
    )
    """
    light green cap

    light green cap.
    """

    lavender = CodeSystemConcept(
        {"code": "lavender", "definition": "lavender cap.", "display": "lavender cap"}
    )
    """
    lavender cap

    lavender cap.
    """

    brown = CodeSystemConcept(
        {"code": "brown", "definition": "brown cap.", "display": "brown cap"}
    )
    """
    brown cap

    brown cap.
    """

    white = CodeSystemConcept(
        {"code": "white", "definition": "white cap.", "display": "white cap"}
    )
    """
    white cap

    white cap.
    """

    pink = CodeSystemConcept(
        {"code": "pink", "definition": "pink cap.", "display": "pink cap"}
    )
    """
    pink cap

    pink cap.
    """

    class Meta:
        resource = _resource
