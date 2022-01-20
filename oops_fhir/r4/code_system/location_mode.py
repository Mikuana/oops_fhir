from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["LocationMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class LocationMode:
    """
    LocationMode

    Indicates whether a resource instance represents a specific location or
a class of locations.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/location-mode
    """

    instance = CodeSystemConcept(
        {
            "code": "instance",
            "definition": "The Location resource represents a specific instance of a location (e.g. Operating Theatre 1A).",
            "display": "Instance",
        }
    )
    """
    Instance

    The Location resource represents a specific instance of a location (e.g. Operating Theatre 1A).
    """

    kind = CodeSystemConcept(
        {
            "code": "kind",
            "definition": "The Location represents a class of locations (e.g. Any Operating Theatre) although this class of locations could be constrained within a specific boundary (such as organization, or parent location, address etc.).",
            "display": "Kind",
        }
    )
    """
    Kind

    The Location represents a class of locations (e.g. Any Operating Theatre) although this class of locations could be constrained within a specific boundary (such as organization, or parent location, address etc.).
    """

    class Meta:
        resource = _resource
