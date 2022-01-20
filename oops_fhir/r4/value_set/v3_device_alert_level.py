from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_device_alert_level import (
    v3DeviceAlertLevel as v3DeviceAlertLevel_,
)


__all__ = ["v3DeviceAlertLevel"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3DeviceAlertLevel(v3DeviceAlertLevel_):
    """
    v3 Code System DeviceAlertLevel

     Domain values for the Device.Alert_levelCode

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-DeviceAlertLevel
    """

    class Meta:
        resource = _resource
