from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_relationship_type import v3ActRelationshipType


__all__ = ["v3ActRelationshipFulfills"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActRelationshipFulfills(v3ActRelationshipType):
    """
    V3 Value SetActRelationshipFulfills

     The source act fulfills (in whole or in part) the target act. Source
act must be in a mood equal or more actual than the target act.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ActRelationshipFulfills
    """

    class Meta:
        resource = _resource
