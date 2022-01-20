from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["OperationKind"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class OperationKind:
    """
    OperationKind

    Whether an operation is a normal operation or a query.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/operation-kind
    """

    operation = CodeSystemConcept(
        {
            "code": "operation",
            "definition": "This operation is invoked as an operation.",
            "display": "Operation",
        }
    )
    """
    Operation

    This operation is invoked as an operation.
    """

    query = CodeSystemConcept(
        {
            "code": "query",
            "definition": "This operation is a named query, invoked using the search mechanism.",
            "display": "Query",
        }
    )
    """
    Query

    This operation is a named query, invoked using the search mechanism.
    """

    class Meta:
        resource = _resource
