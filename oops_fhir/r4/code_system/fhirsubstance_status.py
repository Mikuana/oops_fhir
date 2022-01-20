from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["FHIRSubstanceStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class FHIRSubstanceStatus:
    """
    FHIRSubstanceStatus

    A code to indicate if the substance is actively used.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/substance-status
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "The substance is considered for use or reference.",
            "display": "Active",
        }
    )
    """
    Active

    The substance is considered for use or reference.
    """

    inactive = CodeSystemConcept(
        {
            "code": "inactive",
            "definition": "The substance is considered for reference, but not for use.",
            "display": "Inactive",
        }
    )
    """
    Inactive

    The substance is considered for reference, but not for use.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The substance was entered in error.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The substance was entered in error.
    """

    class Meta:
        resource = _resource
