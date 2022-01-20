from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.device_metric_calibration_type import (
    DeviceMetricCalibrationType as DeviceMetricCalibrationType_,
)


__all__ = ["DeviceMetricCalibrationType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DeviceMetricCalibrationType(DeviceMetricCalibrationType_):
    """
    DeviceMetricCalibrationType

    Describes the type of a metric calibration.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/metric-calibration-type
    """

    class Meta:
        resource = _resource
