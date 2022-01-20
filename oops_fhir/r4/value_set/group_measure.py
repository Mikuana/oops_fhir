from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.group_measure import GroupMeasure as GroupMeasure_


__all__ = ["GroupMeasure"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class GroupMeasure(GroupMeasure_):
    """
    GroupMeasure

    Possible group measure aggregates (E.g. Mean, Median).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/group-measure
    """

    class Meta:
        resource = _resource
