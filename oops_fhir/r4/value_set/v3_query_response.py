from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_query_response import (
    v3QueryResponse as v3QueryResponse_,
)


__all__ = ["v3QueryResponse"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3QueryResponse(v3QueryResponse_):
    """
    v3 Code System QueryResponse

     A code classifying the general nature of the response to a given query.
Includes whether or not data was found, or whether an error occurred.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-QueryResponse
    """

    class Meta:
        resource = _resource
