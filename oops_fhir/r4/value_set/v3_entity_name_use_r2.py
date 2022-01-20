from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_entity_name_use_r2 import (
    v3EntityNameUseR2 as v3EntityNameUseR2_,
)


__all__ = ["v3EntityNameUseR2"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityNameUseR2(v3EntityNameUseR2_):
    """
    v3 Code System EntityNameUseR2

      Description:  A set of codes advising a system or user which name in a
set of names to select for a given purpose.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-EntityNameUseR2
    """

    class Meta:
        resource = _resource
