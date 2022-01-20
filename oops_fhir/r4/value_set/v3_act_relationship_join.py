from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_relationship_join import (
    v3ActRelationshipJoin as v3ActRelationshipJoin_,
)


__all__ = ["v3ActRelationshipJoin"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActRelationshipJoin(v3ActRelationshipJoin_):
    """
    v3 Code System ActRelationshipJoin

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ActRelationshipJoin
    """

    class Meta:
        resource = _resource
