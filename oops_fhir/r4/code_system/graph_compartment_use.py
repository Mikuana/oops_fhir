from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["GraphCompartmentUse"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class GraphCompartmentUse:
    """
    GraphCompartmentUse

    Defines how a compartment rule is used.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/graph-compartment-use
    """

    condition = CodeSystemConcept(
        {
            "code": "condition",
            "definition": "This compartment rule is a condition for whether the rule applies.",
            "display": "Condition",
        }
    )
    """
    Condition

    This compartment rule is a condition for whether the rule applies.
    """

    requirement = CodeSystemConcept(
        {
            "code": "requirement",
            "definition": "This compartment rule is enforced on any relationships that meet the conditions.",
            "display": "Requirement",
        }
    )
    """
    Requirement

    This compartment rule is enforced on any relationships that meet the conditions.
    """

    class Meta:
        resource = _resource
