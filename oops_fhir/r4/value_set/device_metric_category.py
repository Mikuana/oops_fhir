from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.device_metric_category import (
    DeviceMetricCategory as DeviceMetricCategory_,
)


__all__ = ["DeviceMetricCategory"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DeviceMetricCategory(DeviceMetricCategory_):
    """
    DeviceMetricCategory

    Describes the category of the metric.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/metric-category
    """

    class Meta:
        resource = _resource
