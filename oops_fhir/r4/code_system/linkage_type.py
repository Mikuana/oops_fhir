from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["LinkageType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class LinkageType:
    """
    LinkageType

    Used to distinguish different roles a resource can play within a set of
linked resources.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/linkage-type
    """

    source = CodeSystemConcept(
        {
            "code": "source",
            "definition": 'The resource represents the "source of truth" (from the perspective of this Linkage resource) for the underlying event/condition/etc.',
            "display": "Source of Truth",
        }
    )
    """
    Source of Truth

    The resource represents the "source of truth" (from the perspective of this Linkage resource) for the underlying event/condition/etc.
    """

    alternate = CodeSystemConcept(
        {
            "code": "alternate",
            "definition": "The resource represents an alternative view of the underlying event/condition/etc.  The resource may still be actively maintained, even though it is not considered to be the source of truth.",
            "display": "Alternate Record",
        }
    )
    """
    Alternate Record

    The resource represents an alternative view of the underlying event/condition/etc.  The resource may still be actively maintained, even though it is not considered to be the source of truth.
    """

    historical = CodeSystemConcept(
        {
            "code": "historical",
            "definition": "The resource represents an obsolete record of the underlying event/condition/etc.  It is not expected to be actively maintained.",
            "display": "Historical/Obsolete Record",
        }
    )
    """
    Historical/Obsolete Record

    The resource represents an obsolete record of the underlying event/condition/etc.  It is not expected to be actively maintained.
    """

    class Meta:
        resource = _resource
