from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AssertionDirectionType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AssertionDirectionType:
    """
    AssertionDirectionType

    The type of direction to use for assertion.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/assert-direction-codes
    """

    response = CodeSystemConcept(
        {
            "code": "response",
            "definition": "The assertion is evaluated on the response. This is the default value.",
            "display": "response",
        }
    )
    """
    response

    The assertion is evaluated on the response. This is the default value.
    """

    request = CodeSystemConcept(
        {
            "code": "request",
            "definition": "The assertion is evaluated on the request.",
            "display": "request",
        }
    )
    """
    request

    The assertion is evaluated on the request.
    """

    class Meta:
        resource = _resource
