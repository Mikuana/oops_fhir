from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["TestScriptRequestMethodCode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class TestScriptRequestMethodCode:
    """
    TestScriptRequestMethodCode

    The allowable request method or HTTP operation codes.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/http-operations
    """

    delete = CodeSystemConcept(
        {"code": "delete", "definition": "HTTP DELETE operation.", "display": "DELETE"}
    )
    """
    DELETE

    HTTP DELETE operation.
    """

    get = CodeSystemConcept(
        {"code": "get", "definition": "HTTP GET operation.", "display": "GET"}
    )
    """
    GET

    HTTP GET operation.
    """

    options = CodeSystemConcept(
        {
            "code": "options",
            "definition": "HTTP OPTIONS operation.",
            "display": "OPTIONS",
        }
    )
    """
    OPTIONS

    HTTP OPTIONS operation.
    """

    patch = CodeSystemConcept(
        {"code": "patch", "definition": "HTTP PATCH operation.", "display": "PATCH"}
    )
    """
    PATCH

    HTTP PATCH operation.
    """

    post = CodeSystemConcept(
        {"code": "post", "definition": "HTTP POST operation.", "display": "POST"}
    )
    """
    POST

    HTTP POST operation.
    """

    put = CodeSystemConcept(
        {"code": "put", "definition": "HTTP PUT operation.", "display": "PUT"}
    )
    """
    PUT

    HTTP PUT operation.
    """

    head = CodeSystemConcept(
        {"code": "head", "definition": "HTTP HEAD operation.", "display": "HEAD"}
    )
    """
    HEAD

    HTTP HEAD operation.
    """

    class Meta:
        resource = _resource
