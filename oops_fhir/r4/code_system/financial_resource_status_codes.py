from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["FinancialResourceStatusCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class FinancialResourceStatusCodes:
    """
    Financial Resource Status Codes

    This value set includes Status codes.

    Status: draft - Version: 4.0.1

    Copyright HL7 International.

    http://hl7.org/fhir/fm-status
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "The instance is currently in-force.",
            "display": "Active",
        }
    )
    """
    Active

    The instance is currently in-force.
    """

    cancelled = CodeSystemConcept(
        {
            "code": "cancelled",
            "definition": "The instance is withdrawn, rescinded or reversed.",
            "display": "Cancelled",
        }
    )
    """
    Cancelled

    The instance is withdrawn, rescinded or reversed.
    """

    draft = CodeSystemConcept(
        {
            "code": "draft",
            "definition": "A new instance the contents of which is not complete.",
            "display": "Draft",
        }
    )
    """
    Draft

    A new instance the contents of which is not complete.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The instance was entered in error.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The instance was entered in error.
    """

    class Meta:
        resource = _resource
