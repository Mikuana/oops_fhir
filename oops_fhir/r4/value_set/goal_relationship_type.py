from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.goal_relationship_type import (
    GoalRelationshipType as GoalRelationshipType_,
)


__all__ = ["GoalRelationshipType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class GoalRelationshipType(GoalRelationshipType_):
    """
    GoalRelationshipType

    Types of relationships between two goals.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/goal-relationship-type
    """

    class Meta:
        resource = _resource
