from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.action_relationship_type import (
    ActionRelationshipType as ActionRelationshipType_,
)


__all__ = ["ActionRelationshipType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ActionRelationshipType(ActionRelationshipType_):
    """
    ActionRelationshipType

    Defines the types of relationships between actions.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/action-relationship-type
    """

    class Meta:
        resource = _resource
