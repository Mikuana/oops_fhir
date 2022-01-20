from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.fhirdevice_status_reason import (
    FHIRDeviceStatusReason as FHIRDeviceStatusReason_,
)


__all__ = ["FHIRDeviceStatusReason"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FHIRDeviceStatusReason(FHIRDeviceStatusReason_):
    """
    FHIRDeviceStatusReason

    The availability status reason of the device.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/device-status-reason
    """

    class Meta:
        resource = _resource
