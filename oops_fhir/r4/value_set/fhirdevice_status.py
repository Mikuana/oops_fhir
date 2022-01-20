from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.fhirdevice_status import (
    FHIRDeviceStatus as FHIRDeviceStatus_,
)


__all__ = ["FHIRDeviceStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FHIRDeviceStatus(FHIRDeviceStatus_):
    """
    FHIRDeviceStatus

    The availability status of the device.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/device-status
    """

    class Meta:
        resource = _resource
