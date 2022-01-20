from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["FlagStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class FlagStatus:
    """
    FlagStatus

    Indicates whether this flag is active and needs to be displayed to a
user, or whether it is no longer needed or was entered in error.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/flag-status
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "A current flag that should be displayed to a user. A system may use the category to determine which user roles should view the flag.",
            "display": "Active",
        }
    )
    """
    Active

    A current flag that should be displayed to a user. A system may use the category to determine which user roles should view the flag.
    """

    inactive = CodeSystemConcept(
        {
            "code": "inactive",
            "definition": "The flag no longer needs to be displayed.",
            "display": "Inactive",
        }
    )
    """
    Inactive

    The flag no longer needs to be displayed.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The flag was added in error and should no longer be displayed.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The flag was added in error and should no longer be displayed.
    """

    class Meta:
        resource = _resource
