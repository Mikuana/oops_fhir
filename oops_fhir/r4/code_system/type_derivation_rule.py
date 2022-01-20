from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["TypeDerivationRule"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class TypeDerivationRule:
    """
    TypeDerivationRule

    How a type relates to its baseDefinition.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/type-derivation-rule
    """

    specialization = CodeSystemConcept(
        {
            "code": "specialization",
            "definition": "This definition defines a new type that adds additional elements to the base type.",
            "display": "Specialization",
        }
    )
    """
    Specialization

    This definition defines a new type that adds additional elements to the base type.
    """

    constraint = CodeSystemConcept(
        {
            "code": "constraint",
            "definition": "This definition adds additional rules to an existing concrete type.",
            "display": "Constraint",
        }
    )
    """
    Constraint

    This definition adds additional rules to an existing concrete type.
    """

    class Meta:
        resource = _resource
