from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_relationship_type import v3ActRelationshipType


__all__ = ["v3ActRelationshipConditional"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActRelationshipConditional(v3ActRelationshipType):
    """
    V3 Value SetActRelationshipConditional

     Specifies under what circumstances (target Act) the source-Act may,
must, must not or has occurred

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ActRelationshipConditional
    """

    class Meta:
        resource = _resource
