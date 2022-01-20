from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_relationship_type import (
    v3ActRelationshipType as v3ActRelationshipType_,
)


__all__ = ["v3ActRelationshipType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActRelationshipType(v3ActRelationshipType_):
    """
    v3 Code System ActRelationshipType

     The source is an excerpt from the target.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ActRelationshipType
    """

    class Meta:
        resource = _resource
