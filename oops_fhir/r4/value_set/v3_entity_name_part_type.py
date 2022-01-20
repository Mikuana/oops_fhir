from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_entity_name_part_type import (
    v3EntityNamePartType as v3EntityNamePartType_,
)


__all__ = ["v3EntityNamePartType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityNamePartType(v3EntityNamePartType_):
    """
    v3 Code System EntityNamePartType

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-EntityNamePartType
    """

    class Meta:
        resource = _resource
