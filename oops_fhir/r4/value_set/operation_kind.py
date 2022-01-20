from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.operation_kind import OperationKind as OperationKind_


__all__ = ["OperationKind"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class OperationKind(OperationKind_):
    """
    OperationKind

    Whether an operation is a normal operation or a query.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/operation-kind
    """

    class Meta:
        resource = _resource
