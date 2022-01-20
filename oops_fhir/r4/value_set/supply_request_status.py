from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.supply_request_status import (
    SupplyRequestStatus as SupplyRequestStatus_,
)


__all__ = ["SupplyRequestStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SupplyRequestStatus(SupplyRequestStatus_):
    """
    SupplyRequestStatus

    Status of the supply request.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/supplyrequest-status
    """

    class Meta:
        resource = _resource
