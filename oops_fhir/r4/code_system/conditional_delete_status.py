from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ConditionalDeleteStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ConditionalDeleteStatus:
    """
    ConditionalDeleteStatus

    A code that indicates how the server supports conditional delete.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/conditional-delete-status
    """

    not_supported = CodeSystemConcept(
        {
            "code": "not-supported",
            "definition": "No support for conditional deletes.",
            "display": "Not Supported",
        }
    )
    """
    Not Supported

    No support for conditional deletes.
    """

    single = CodeSystemConcept(
        {
            "code": "single",
            "definition": "Conditional deletes are supported, but only single resources at a time.",
            "display": "Single Deletes Supported",
        }
    )
    """
    Single Deletes Supported

    Conditional deletes are supported, but only single resources at a time.
    """

    multiple = CodeSystemConcept(
        {
            "code": "multiple",
            "definition": "Conditional deletes are supported, and multiple resources can be deleted in a single interaction.",
            "display": "Multiple Deletes Supported",
        }
    )
    """
    Multiple Deletes Supported

    Conditional deletes are supported, and multiple resources can be deleted in a single interaction.
    """

    class Meta:
        resource = _resource
