from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExplanationOfBenefitStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExplanationOfBenefitStatus:
    """
    ExplanationOfBenefitStatus

    A code specifying the state of the resource instance.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/explanationofbenefit-status
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "The resource instance is currently in-force.",
            "display": "Active",
        }
    )
    """
    Active

    The resource instance is currently in-force.
    """

    cancelled = CodeSystemConcept(
        {
            "code": "cancelled",
            "definition": "The resource instance is withdrawn, rescinded or reversed.",
            "display": "Cancelled",
        }
    )
    """
    Cancelled

    The resource instance is withdrawn, rescinded or reversed.
    """

    draft = CodeSystemConcept(
        {
            "code": "draft",
            "definition": "A new resource instance the contents of which is not complete.",
            "display": "Draft",
        }
    )
    """
    Draft

    A new resource instance the contents of which is not complete.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The resource instance was entered in error.",
            "display": "Entered In Error",
        }
    )
    """
    Entered In Error

    The resource instance was entered in error.
    """

    class Meta:
        resource = _resource
