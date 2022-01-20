from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.operation_parameter_use import (
    OperationParameterUse as OperationParameterUse_,
)


__all__ = ["OperationParameterUse"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class OperationParameterUse(OperationParameterUse_):
    """
    OperationParameterUse

    Whether an operation parameter is an input or an output parameter.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/operation-parameter-use
    """

    class Meta:
        resource = _resource
