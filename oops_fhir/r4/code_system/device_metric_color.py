from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DeviceMetricColor"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DeviceMetricColor:
    """
    DeviceMetricColor

    Describes the typical color of representation.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/metric-color
    """

    black = CodeSystemConcept(
        {
            "code": "black",
            "definition": "Color for representation - black.",
            "display": "Color Black",
        }
    )
    """
    Color Black

    Color for representation - black.
    """

    red = CodeSystemConcept(
        {
            "code": "red",
            "definition": "Color for representation - red.",
            "display": "Color Red",
        }
    )
    """
    Color Red

    Color for representation - red.
    """

    green = CodeSystemConcept(
        {
            "code": "green",
            "definition": "Color for representation - green.",
            "display": "Color Green",
        }
    )
    """
    Color Green

    Color for representation - green.
    """

    yellow = CodeSystemConcept(
        {
            "code": "yellow",
            "definition": "Color for representation - yellow.",
            "display": "Color Yellow",
        }
    )
    """
    Color Yellow

    Color for representation - yellow.
    """

    blue = CodeSystemConcept(
        {
            "code": "blue",
            "definition": "Color for representation - blue.",
            "display": "Color Blue",
        }
    )
    """
    Color Blue

    Color for representation - blue.
    """

    magenta = CodeSystemConcept(
        {
            "code": "magenta",
            "definition": "Color for representation - magenta.",
            "display": "Color Magenta",
        }
    )
    """
    Color Magenta

    Color for representation - magenta.
    """

    cyan = CodeSystemConcept(
        {
            "code": "cyan",
            "definition": "Color for representation - cyan.",
            "display": "Color Cyan",
        }
    )
    """
    Color Cyan

    Color for representation - cyan.
    """

    white = CodeSystemConcept(
        {
            "code": "white",
            "definition": "Color for representation - white.",
            "display": "Color White",
        }
    )
    """
    Color White

    Color for representation - white.
    """

    class Meta:
        resource = _resource
