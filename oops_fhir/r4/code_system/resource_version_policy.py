from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ResourceVersionPolicy"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ResourceVersionPolicy:
    """
    ResourceVersionPolicy

    How the system supports versioning for a resource.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/versioning-policy
    """

    no_version = CodeSystemConcept(
        {
            "code": "no-version",
            "definition": "VersionId meta-property is not supported (server) or used (client).",
            "display": "No VersionId Support",
        }
    )
    """
    No VersionId Support

    VersionId meta-property is not supported (server) or used (client).
    """

    versioned = CodeSystemConcept(
        {
            "code": "versioned",
            "definition": "VersionId meta-property is supported (server) or used (client).",
            "display": "Versioned",
        }
    )
    """
    Versioned

    VersionId meta-property is supported (server) or used (client).
    """

    versioned_update = CodeSystemConcept(
        {
            "code": "versioned-update",
            "definition": "VersionId must be correct for updates (server) or will be specified (If-match header) for updates (client).",
            "display": "VersionId tracked fully",
        }
    )
    """
    VersionId tracked fully

    VersionId must be correct for updates (server) or will be specified (If-match header) for updates (client).
    """

    class Meta:
        resource = _resource
