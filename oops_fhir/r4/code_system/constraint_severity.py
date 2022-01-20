from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ConstraintSeverity"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ConstraintSeverity:
    """
    ConstraintSeverity

    SHALL applications comply with this constraint?

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/constraint-severity
    """

    error = CodeSystemConcept(
        {
            "code": "error",
            "definition": "If the constraint is violated, the resource is not conformant.",
            "display": "Error",
        }
    )
    """
    Error

    If the constraint is violated, the resource is not conformant.
    """

    warning = CodeSystemConcept(
        {
            "code": "warning",
            "definition": "If the constraint is violated, the resource is conformant, but it is not necessarily following best practice.",
            "display": "Warning",
        }
    )
    """
    Warning

    If the constraint is violated, the resource is conformant, but it is not necessarily following best practice.
    """

    class Meta:
        resource = _resource
