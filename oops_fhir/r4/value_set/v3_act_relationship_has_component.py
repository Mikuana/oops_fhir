from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_relationship_type import v3ActRelationshipType


__all__ = ["v3ActRelationshipHasComponent"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActRelationshipHasComponent(v3ActRelationshipType):
    """
    V3 Value SetActRelationshipHasComponent

     A collection of sub-services as steps or subtasks performed for the
source service. Services may be performed sequentially or concurrently.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ActRelationshipHasComponent
    """

    class Meta:
        resource = _resource
