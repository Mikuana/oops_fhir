from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["StructureMapGroupTypeMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class StructureMapGroupTypeMode:
    """
    StructureMapGroupTypeMode

    If this is the default rule set to apply for the source type, or this
combination of types.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/map-group-type-mode
    """

    none = CodeSystemConcept(
        {
            "code": "none",
            "definition": "This group is not a default group for the types.",
            "display": "Not a Default",
        }
    )
    """
    Not a Default

    This group is not a default group for the types.
    """

    types = CodeSystemConcept(
        {
            "code": "types",
            "definition": "This group is a default mapping group for the specified types and for the primary source type.",
            "display": "Default for Type Combination",
        }
    )
    """
    Default for Type Combination

    This group is a default mapping group for the specified types and for the primary source type.
    """

    type_and_types = CodeSystemConcept(
        {
            "code": "type-and-types",
            "definition": "This group is a default mapping group for the specified types.",
            "display": "Default for type + combination",
        }
    )
    """
    Default for type + combination

    This group is a default mapping group for the specified types.
    """

    class Meta:
        resource = _resource
