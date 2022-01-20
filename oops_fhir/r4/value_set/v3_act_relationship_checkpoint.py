from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_relationship_checkpoint import (
    v3ActRelationshipCheckpoint as v3ActRelationshipCheckpoint_,
)


__all__ = ["v3ActRelationshipCheckpoint"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActRelationshipCheckpoint(v3ActRelationshipCheckpoint_):
    """
    v3 Code System ActRelationshipCheckpoint

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ActRelationshipCheckpoint
    """

    class Meta:
        resource = _resource
