from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.device_metric_operational_status import (
    DeviceMetricOperationalStatus as DeviceMetricOperationalStatus_,
)


__all__ = ["DeviceMetricOperationalStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DeviceMetricOperationalStatus(DeviceMetricOperationalStatus_):
    """
    DeviceMetricOperationalStatus

    Describes the operational status of the DeviceMetric.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/metric-operational-status
    """

    class Meta:
        resource = _resource
