from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExpansionParameterSource"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExpansionParameterSource:
    """
    ExpansionParameterSource

    Declares what the source of a parameter is.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/expansion-parameter-source
    """

    input_ = CodeSystemConcept(
        {
            "code": "input",
            "definition": "The parameter was supplied by the client in the $expand request.",
            "display": "Client Input",
        }
    )
    """
    Client Input

    The parameter was supplied by the client in the $expand request.
    """

    server = CodeSystemConcept(
        {
            "code": "server",
            "definition": "The parameter was added by the expansion engine on the server.",
            "display": "Server Engine",
        }
    )
    """
    Server Engine

    The parameter was added by the expansion engine on the server.
    """

    codesystem = CodeSystemConcept(
        {
            "code": "codesystem",
            "definition": "The parameter was added from one the code systems used in the $expand operation.",
            "display": "Code System",
        }
    )
    """
    Code System

    The parameter was added from one the code systems used in the $expand operation.
    """

    class Meta:
        resource = _resource
