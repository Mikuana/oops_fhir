from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.group_type import GroupType as GroupType_


__all__ = ["GroupType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class GroupType(GroupType_):
    """
    GroupType

    Types of resources that are part of group.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/group-type
    """

    class Meta:
        resource = _resource
