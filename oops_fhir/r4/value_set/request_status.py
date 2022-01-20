from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.request_status import RequestStatus as RequestStatus_


__all__ = ["RequestStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class RequestStatus(RequestStatus_):
    """
    RequestStatus

    Codes identifying the lifecycle stage of a request.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/request-status
    """

    class Meta:
        resource = _resource
