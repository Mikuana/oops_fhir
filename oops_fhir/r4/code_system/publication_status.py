from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["PublicationStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class PublicationStatus:
    """
    PublicationStatus

    The lifecycle status of an artifact.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/publication-status
    """

    draft = CodeSystemConcept(
        {
            "code": "draft",
            "definition": "This resource is still under development and is not yet considered to be ready for normal use.",
            "designation": [
                {"language": "ru", "value": "черновик"},
                {"language": "nl", "value": "ontwerp"},
            ],
            "display": "Draft",
        }
    )
    """
    Draft

    This resource is still under development and is not yet considered to be ready for normal use.
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "This resource is ready for normal use.",
            "designation": [
                {"language": "ru", "value": "активный"},
                {"language": "nl", "value": "actief"},
            ],
            "display": "Active",
        }
    )
    """
    Active

    This resource is ready for normal use.
    """

    retired = CodeSystemConcept(
        {
            "code": "retired",
            "definition": "This resource has been withdrawn or superseded and should no longer be used.",
            "designation": [
                {"language": "ru", "value": "удалён"},
                {"language": "nl", "value": "verouderd"},
            ],
            "display": "Retired",
        }
    )
    """
    Retired

    This resource has been withdrawn or superseded and should no longer be used.
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": 'The authoring system does not know which of the status values currently applies for this resource.  Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, it\'s just not known which one.',
            "display": "Unknown",
        }
    )
    """
    Unknown

    The authoring system does not know which of the status values currently applies for this resource.  Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, it's just not known which one.
    """

    class Meta:
        resource = _resource
