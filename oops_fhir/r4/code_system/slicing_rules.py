from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SlicingRules"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SlicingRules:
    """
    SlicingRules

    How slices are interpreted when evaluating an instance.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/resource-slicing-rules
    """

    closed = CodeSystemConcept(
        {
            "code": "closed",
            "definition": "No additional content is allowed other than that described by the slices in this profile.",
            "display": "Closed",
        }
    )
    """
    Closed

    No additional content is allowed other than that described by the slices in this profile.
    """

    open_ = CodeSystemConcept(
        {
            "code": "open",
            "definition": "Additional content is allowed anywhere in the list.",
            "display": "Open",
        }
    )
    """
    Open

    Additional content is allowed anywhere in the list.
    """

    open_at_end = CodeSystemConcept(
        {
            "code": "openAtEnd",
            "definition": "Additional content is allowed, but only at the end of the list. Note that using this requires that the slices be ordered, which makes it hard to share uses. This should only be done where absolutely required.",
            "display": "Open at End",
        }
    )
    """
    Open at End

    Additional content is allowed, but only at the end of the list. Note that using this requires that the slices be ordered, which makes it hard to share uses. This should only be done where absolutely required.
    """

    class Meta:
        resource = _resource
