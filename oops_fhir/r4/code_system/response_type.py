from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ResponseType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ResponseType:
    """
    ResponseType

    The kind of response to a message.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/response-code
    """

    ok = CodeSystemConcept(
        {
            "code": "ok",
            "definition": "The message was accepted and processed without error.",
            "display": "OK",
        }
    )
    """
    OK

    The message was accepted and processed without error.
    """

    transient_error = CodeSystemConcept(
        {
            "code": "transient-error",
            "definition": "Some internal unexpected error occurred - wait and try again. Note - this is usually used for things like database unavailable, which may be expected to resolve, though human intervention may be required.",
            "display": "Transient Error",
        }
    )
    """
    Transient Error

    Some internal unexpected error occurred - wait and try again. Note - this is usually used for things like database unavailable, which may be expected to resolve, though human intervention may be required.
    """

    fatal_error = CodeSystemConcept(
        {
            "code": "fatal-error",
            "definition": "The message was rejected because of a problem with the content. There is no point in re-sending without change. The response narrative SHALL describe the issue.",
            "display": "Fatal Error",
        }
    )
    """
    Fatal Error

    The message was rejected because of a problem with the content. There is no point in re-sending without change. The response narrative SHALL describe the issue.
    """

    class Meta:
        resource = _resource
