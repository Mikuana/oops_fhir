from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.request_priority import (
    RequestPriority as RequestPriority_,
)


__all__ = ["RequestPriority"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class RequestPriority(RequestPriority_):
    """
    Request priority

    The clinical priority of a diagnostic order.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/request-priority
    """

    class Meta:
        resource = _resource
