from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["LocationStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class LocationStatus:
    """
    LocationStatus

    Indicates whether the location is still in use.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/location-status
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "The location is operational.",
            "display": "Active",
        }
    )
    """
    Active

    The location is operational.
    """

    suspended = CodeSystemConcept(
        {
            "code": "suspended",
            "definition": "The location is temporarily closed.",
            "display": "Suspended",
        }
    )
    """
    Suspended

    The location is temporarily closed.
    """

    inactive = CodeSystemConcept(
        {
            "code": "inactive",
            "definition": "The location is no longer used.",
            "display": "Inactive",
        }
    )
    """
    Inactive

    The location is no longer used.
    """

    class Meta:
        resource = _resource
