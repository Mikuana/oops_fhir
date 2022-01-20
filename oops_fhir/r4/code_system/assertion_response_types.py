from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AssertionResponseTypes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AssertionResponseTypes:
    """
    AssertionResponseTypes

    The type of response code to use for assertion.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/assert-response-code-types
    """

    okay = CodeSystemConcept(
        {"code": "okay", "definition": "Response code is 200.", "display": "okay"}
    )
    """
    okay

    Response code is 200.
    """

    created = CodeSystemConcept(
        {"code": "created", "definition": "Response code is 201.", "display": "created"}
    )
    """
    created

    Response code is 201.
    """

    no_content = CodeSystemConcept(
        {
            "code": "noContent",
            "definition": "Response code is 204.",
            "display": "noContent",
        }
    )
    """
    noContent

    Response code is 204.
    """

    not_modified = CodeSystemConcept(
        {
            "code": "notModified",
            "definition": "Response code is 304.",
            "display": "notModified",
        }
    )
    """
    notModified

    Response code is 304.
    """

    bad = CodeSystemConcept(
        {"code": "bad", "definition": "Response code is 400.", "display": "bad"}
    )
    """
    bad

    Response code is 400.
    """

    forbidden = CodeSystemConcept(
        {
            "code": "forbidden",
            "definition": "Response code is 403.",
            "display": "forbidden",
        }
    )
    """
    forbidden

    Response code is 403.
    """

    not_found = CodeSystemConcept(
        {
            "code": "notFound",
            "definition": "Response code is 404.",
            "display": "notFound",
        }
    )
    """
    notFound

    Response code is 404.
    """

    method_not_allowed = CodeSystemConcept(
        {
            "code": "methodNotAllowed",
            "definition": "Response code is 405.",
            "display": "methodNotAllowed",
        }
    )
    """
    methodNotAllowed

    Response code is 405.
    """

    conflict = CodeSystemConcept(
        {
            "code": "conflict",
            "definition": "Response code is 409.",
            "display": "conflict",
        }
    )
    """
    conflict

    Response code is 409.
    """

    gone = CodeSystemConcept(
        {"code": "gone", "definition": "Response code is 410.", "display": "gone"}
    )
    """
    gone

    Response code is 410.
    """

    precondition_failed = CodeSystemConcept(
        {
            "code": "preconditionFailed",
            "definition": "Response code is 412.",
            "display": "preconditionFailed",
        }
    )
    """
    preconditionFailed

    Response code is 412.
    """

    unprocessable = CodeSystemConcept(
        {
            "code": "unprocessable",
            "definition": "Response code is 422.",
            "display": "unprocessable",
        }
    )
    """
    unprocessable

    Response code is 422.
    """

    class Meta:
        resource = _resource
