from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_modify_indicator import (
    v3ModifyIndicator as v3ModifyIndicator_,
)


__all__ = ["v3ModifyIndicator"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ModifyIndicator(v3ModifyIndicator_):
    """
    v3 Code System ModifyIndicator

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ModifyIndicator
    """

    class Meta:
        resource = _resource
