from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["OperationParameterUse"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class OperationParameterUse:
    """
    OperationParameterUse

    Whether an operation parameter is an input or an output parameter.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/operation-parameter-use
    """

    in_ = CodeSystemConcept(
        {"code": "in", "definition": "This is an input parameter.", "display": "In"}
    )
    """
    In

    This is an input parameter.
    """

    out = CodeSystemConcept(
        {"code": "out", "definition": "This is an output parameter.", "display": "Out"}
    )
    """
    Out

    This is an output parameter.
    """

    class Meta:
        resource = _resource
