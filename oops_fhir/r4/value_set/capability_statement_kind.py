from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.capability_statement_kind import (
    CapabilityStatementKind as CapabilityStatementKind_,
)


__all__ = ["CapabilityStatementKind"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CapabilityStatementKind(CapabilityStatementKind_):
    """
    CapabilityStatementKind

    How a capability statement is intended to be used.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/capability-statement-kind
    """

    class Meta:
        resource = _resource
