from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_query_priority import (
    v3QueryPriority as v3QueryPriority_,
)


__all__ = ["v3QueryPriority"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3QueryPriority(v3QueryPriority_):
    """
    v3 Code System QueryPriority

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-QueryPriority
    """

    class Meta:
        resource = _resource
