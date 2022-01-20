from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["HTTPVerb"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class HTTPVerb:
    """
    HTTPVerb

    HTTP verbs (in the HTTP command line). See [HTTP
rfc](https://tools.ietf.org/html/rfc7231) for details.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/http-verb
    """

    get = CodeSystemConcept(
        {"code": "GET", "definition": "HTTP GET Command.", "display": "GET"}
    )
    """
    GET

    HTTP GET Command.
    """

    head = CodeSystemConcept(
        {"code": "HEAD", "definition": "HTTP HEAD Command.", "display": "HEAD"}
    )
    """
    HEAD

    HTTP HEAD Command.
    """

    post = CodeSystemConcept(
        {"code": "POST", "definition": "HTTP POST Command.", "display": "POST"}
    )
    """
    POST

    HTTP POST Command.
    """

    put = CodeSystemConcept(
        {"code": "PUT", "definition": "HTTP PUT Command.", "display": "PUT"}
    )
    """
    PUT

    HTTP PUT Command.
    """

    delete = CodeSystemConcept(
        {"code": "DELETE", "definition": "HTTP DELETE Command.", "display": "DELETE"}
    )
    """
    DELETE

    HTTP DELETE Command.
    """

    patch = CodeSystemConcept(
        {"code": "PATCH", "definition": "HTTP PATCH Command.", "display": "PATCH"}
    )
    """
    PATCH

    HTTP PATCH Command.
    """

    class Meta:
        resource = _resource
