from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_entity_name_part_type_r2 import (
    v3EntityNamePartTypeR2 as v3EntityNamePartTypeR2_,
)


__all__ = ["v3EntityNamePartTypeR2"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityNamePartTypeR2(v3EntityNamePartTypeR2_):
    """
    v3 Code System EntityNamePartTypeR2

      Description:  Indicates whether the name part is a given name, family
name, prefix, suffix, etc.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-EntityNamePartTypeR2
    """

    class Meta:
        resource = _resource
