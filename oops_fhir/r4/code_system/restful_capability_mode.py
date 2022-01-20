from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["RestfulCapabilityMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class RestfulCapabilityMode:
    """
    RestfulCapabilityMode

    The mode of a RESTful capability statement.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/restful-capability-mode
    """

    client = CodeSystemConcept(
        {
            "code": "client",
            "definition": "The application acts as a client for this resource.",
            "display": "Client",
        }
    )
    """
    Client

    The application acts as a client for this resource.
    """

    server = CodeSystemConcept(
        {
            "code": "server",
            "definition": "The application acts as a server for this resource.",
            "display": "Server",
        }
    )
    """
    Server

    The application acts as a server for this resource.
    """

    class Meta:
        resource = _resource
