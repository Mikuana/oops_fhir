from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_query_request_limit import (
    v3QueryRequestLimit as v3QueryRequestLimit_,
)


__all__ = ["v3QueryRequestLimit"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3QueryRequestLimit(v3QueryRequestLimit_):
    """
    v3 Code System QueryRequestLimit

      Definition:  Defines the units associated with the magnitude of the
maximum size limit of a query response that can be accepted by the
requesting application.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-QueryRequestLimit
    """

    class Meta:
        resource = _resource
