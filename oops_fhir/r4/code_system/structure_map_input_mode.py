from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["StructureMapInputMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class StructureMapInputMode:
    """
    StructureMapInputMode

    Mode for this instance of data.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/map-input-mode
    """

    source = CodeSystemConcept(
        {
            "code": "source",
            "definition": "Names an input instance used a source for mapping.",
            "display": "Source Instance",
        }
    )
    """
    Source Instance

    Names an input instance used a source for mapping.
    """

    target = CodeSystemConcept(
        {
            "code": "target",
            "definition": "Names an instance that is being populated.",
            "display": "Target Instance",
        }
    )
    """
    Target Instance

    Names an instance that is being populated.
    """

    class Meta:
        resource = _resource
