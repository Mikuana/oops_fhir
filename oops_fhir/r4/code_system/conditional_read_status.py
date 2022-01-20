from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ConditionalReadStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ConditionalReadStatus:
    """
    ConditionalReadStatus

    A code that indicates how the server supports conditional read.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/conditional-read-status
    """

    not_supported = CodeSystemConcept(
        {
            "code": "not-supported",
            "definition": "No support for conditional reads.",
            "display": "Not Supported",
        }
    )
    """
    Not Supported

    No support for conditional reads.
    """

    modified_since = CodeSystemConcept(
        {
            "code": "modified-since",
            "definition": "Conditional reads are supported, but only with the If-Modified-Since HTTP Header.",
            "display": "If-Modified-Since",
        }
    )
    """
    If-Modified-Since

    Conditional reads are supported, but only with the If-Modified-Since HTTP Header.
    """

    not_match = CodeSystemConcept(
        {
            "code": "not-match",
            "definition": "Conditional reads are supported, but only with the If-None-Match HTTP Header.",
            "display": "If-None-Match",
        }
    )
    """
    If-None-Match

    Conditional reads are supported, but only with the If-None-Match HTTP Header.
    """

    full_support = CodeSystemConcept(
        {
            "code": "full-support",
            "definition": "Conditional reads are supported, with both If-Modified-Since and If-None-Match HTTP Headers.",
            "display": "Full Support",
        }
    )
    """
    Full Support

    Conditional reads are supported, with both If-Modified-Since and If-None-Match HTTP Headers.
    """

    class Meta:
        resource = _resource
