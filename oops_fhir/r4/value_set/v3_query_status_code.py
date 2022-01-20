from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_query_status_code import (
    v3QueryStatusCode as v3QueryStatusCode_,
)


__all__ = ["v3QueryStatusCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3QueryStatusCode(v3QueryStatusCode_):
    """
    v3 Code System QueryStatusCode

     A code specifying the state of the Query.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-QueryStatusCode
    """

    class Meta:
        resource = _resource
