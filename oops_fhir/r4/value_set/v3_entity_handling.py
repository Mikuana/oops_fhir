from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_entity_handling import (
    v3EntityHandling as v3EntityHandling_,
)


__all__ = ["v3EntityHandling"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityHandling(v3EntityHandling_):
    """
    v3 Code System EntityHandling

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-EntityHandling
    """

    class Meta:
        resource = _resource
