from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["StructureMapModelMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class StructureMapModelMode:
    """
    StructureMapModelMode

    How the referenced structure is used in this mapping.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/map-model-mode
    """

    source = CodeSystemConcept(
        {
            "code": "source",
            "definition": "This structure describes an instance passed to the mapping engine that is used a source of data.",
            "display": "Source Structure Definition",
        }
    )
    """
    Source Structure Definition

    This structure describes an instance passed to the mapping engine that is used a source of data.
    """

    queried = CodeSystemConcept(
        {
            "code": "queried",
            "definition": "This structure describes an instance that the mapping engine may ask for that is used a source of data.",
            "display": "Queried Structure Definition",
        }
    )
    """
    Queried Structure Definition

    This structure describes an instance that the mapping engine may ask for that is used a source of data.
    """

    target = CodeSystemConcept(
        {
            "code": "target",
            "definition": "This structure describes an instance passed to the mapping engine that is used a target of data.",
            "display": "Target Structure Definition",
        }
    )
    """
    Target Structure Definition

    This structure describes an instance passed to the mapping engine that is used a target of data.
    """

    produced = CodeSystemConcept(
        {
            "code": "produced",
            "definition": "This structure describes an instance that the mapping engine may ask to create that is used a target of data.",
            "display": "Produced Structure Definition",
        }
    )
    """
    Produced Structure Definition

    This structure describes an instance that the mapping engine may ask to create that is used a target of data.
    """

    class Meta:
        resource = _resource
