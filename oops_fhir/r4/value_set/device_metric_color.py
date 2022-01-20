from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.device_metric_color import (
    DeviceMetricColor as DeviceMetricColor_,
)


__all__ = ["DeviceMetricColor"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DeviceMetricColor(DeviceMetricColor_):
    """
    DeviceMetricColor

    Describes the typical color of representation.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/metric-color
    """

    class Meta:
        resource = _resource
