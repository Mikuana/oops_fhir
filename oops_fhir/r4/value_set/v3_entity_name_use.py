from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_entity_name_use import (
    v3EntityNameUse as v3EntityNameUse_,
)


__all__ = ["v3EntityNameUse"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityNameUse(v3EntityNameUse_):
    """
    v3 Code System EntityNameUse

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-EntityNameUse
    """

    class Meta:
        resource = _resource
