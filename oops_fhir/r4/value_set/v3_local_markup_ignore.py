from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_local_markup_ignore import (
    v3LocalMarkupIgnore as v3LocalMarkupIgnore_,
)


__all__ = ["v3LocalMarkupIgnore"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3LocalMarkupIgnore(v3LocalMarkupIgnore_):
    """
    v3 Code System LocalMarkupIgnore

     Tells a receiver to ignore just the local markup tags (local_markup,
local_header, local_attr) when value="markup", or to ignore the local
markup tags and all contained content when value="all"

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-LocalMarkupIgnore
    """

    class Meta:
        resource = _resource
