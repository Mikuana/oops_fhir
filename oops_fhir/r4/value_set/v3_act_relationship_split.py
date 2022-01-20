from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_relationship_split import (
    v3ActRelationshipSplit as v3ActRelationshipSplit_,
)


__all__ = ["v3ActRelationshipSplit"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActRelationshipSplit(v3ActRelationshipSplit_):
    """
    v3 Code System ActRelationshipSplit

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ActRelationshipSplit
    """

    class Meta:
        resource = _resource
