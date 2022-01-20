from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.guidance_response_status import (
    GuidanceResponseStatus as GuidanceResponseStatus_,
)


__all__ = ["GuidanceResponseStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class GuidanceResponseStatus(GuidanceResponseStatus_):
    """
    GuidanceResponseStatus

    The status of a guidance response.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/guidance-response-status
    """

    class Meta:
        resource = _resource
