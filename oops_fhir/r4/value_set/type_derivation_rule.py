from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.type_derivation_rule import (
    TypeDerivationRule as TypeDerivationRule_,
)


__all__ = ["TypeDerivationRule"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TypeDerivationRule(TypeDerivationRule_):
    """
    TypeDerivationRule

    How a type relates to its baseDefinition.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/type-derivation-rule
    """

    class Meta:
        resource = _resource
