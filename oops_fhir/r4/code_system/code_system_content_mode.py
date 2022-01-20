from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CodeSystemContentMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CodeSystemContentMode:
    """
    CodeSystemContentMode

    The extent of the content of the code system (the concepts and codes it
defines) are represented in a code system resource.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/codesystem-content-mode
    """

    not_present = CodeSystemConcept(
        {
            "code": "not-present",
            "definition": "None of the concepts defined by the code system are included in the code system resource.",
            "display": "Not Present",
        }
    )
    """
    Not Present

    None of the concepts defined by the code system are included in the code system resource.
    """

    example = CodeSystemConcept(
        {
            "code": "example",
            "definition": "A few representative concepts are included in the code system resource. There is no useful intent in the subset choice and there's no process to make it workable: it's not intended to be workable.",
            "display": "Example",
        }
    )
    """
    Example

    A few representative concepts are included in the code system resource. There is no useful intent in the subset choice and there's no process to make it workable: it's not intended to be workable.
    """

    fragment = CodeSystemConcept(
        {
            "code": "fragment",
            "definition": "A subset of the code system concepts are included in the code system resource. This is a curated subset released for a specific purpose under the governance of the code system steward, and that the intent, bounds and consequences of the fragmentation are clearly defined in the fragment or the code system documentation. Fragments are also known as partitions.",
            "display": "Fragment",
        }
    )
    """
    Fragment

    A subset of the code system concepts are included in the code system resource. This is a curated subset released for a specific purpose under the governance of the code system steward, and that the intent, bounds and consequences of the fragmentation are clearly defined in the fragment or the code system documentation. Fragments are also known as partitions.
    """

    complete = CodeSystemConcept(
        {
            "code": "complete",
            "definition": "All the concepts defined by the code system are included in the code system resource.",
            "display": "Complete",
        }
    )
    """
    Complete

    All the concepts defined by the code system are included in the code system resource.
    """

    supplement = CodeSystemConcept(
        {
            "code": "supplement",
            "definition": "The resource doesn't define any new concepts; it just provides additional designations and properties to another code system.",
            "display": "Supplement",
        }
    )
    """
    Supplement

    The resource doesn't define any new concepts; it just provides additional designations and properties to another code system.
    """

    class Meta:
        resource = _resource
