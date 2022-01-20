from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["messageheaderresponserequest"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class messageheaderresponserequest:
    """
    messageheader-response-request

    HL7-defined table of codes which identify conditions under which
acknowledgments are required to be returned in response to a message.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/messageheader-response-request
    """

    always = CodeSystemConcept(
        {
            "code": "always",
            "definition": "initiator expects a response for this message.",
            "display": "Always",
        }
    )
    """
    Always

    initiator expects a response for this message.
    """

    on_error = CodeSystemConcept(
        {
            "code": "on-error",
            "definition": "initiator expects a response only if in error.",
            "display": "Error/reject conditions only",
        }
    )
    """
    Error/reject conditions only

    initiator expects a response only if in error.
    """

    never = CodeSystemConcept(
        {
            "code": "never",
            "definition": "initiator does not expect a response.",
            "display": "Never",
        }
    )
    """
    Never

    initiator does not expect a response.
    """

    on_success = CodeSystemConcept(
        {
            "code": "on-success",
            "definition": "initiator expects a response only if successful.",
            "display": "Successful completion only",
        }
    )
    """
    Successful completion only

    initiator expects a response only if successful.
    """

    class Meta:
        resource = _resource
