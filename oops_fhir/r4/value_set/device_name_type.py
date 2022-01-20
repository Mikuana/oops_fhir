from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.device_name_type import DeviceNameType as DeviceNameType_


__all__ = ["DeviceNameType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DeviceNameType(DeviceNameType_):
    """
    DeviceNameType

    The type of name the device is referred by.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/device-nametype
    """

    class Meta:
        resource = _resource
