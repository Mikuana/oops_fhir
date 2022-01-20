from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_data_operation import (
    v3DataOperation as v3DataOperation_,
)


__all__ = ["v3DataOperation"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3DataOperation(v3DataOperation_):
    """
    v3 Code System DataOperation

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-DataOperation
    """

    class Meta:
        resource = _resource
