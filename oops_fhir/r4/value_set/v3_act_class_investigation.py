from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_class import v3ActClass


__all__ = ["v3ActClassInvestigation"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActClassInvestigation(v3ActClass):
    """
    V3 Value SetActClassInvestigation

     An formalized inquiry into the circumstances surrounding a particular
unplanned event or potential event for the purposes of identifying
possible causes and contributing factors for the event. This
investigation could be conducted at a local institutional level or at
the level of a local or national government.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ActClassInvestigation
    """

    class Meta:
        resource = _resource
