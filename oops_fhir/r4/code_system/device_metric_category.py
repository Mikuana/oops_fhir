from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DeviceMetricCategory"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DeviceMetricCategory:
    """
    DeviceMetricCategory

    Describes the category of the metric.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/metric-category
    """

    measurement = CodeSystemConcept(
        {
            "code": "measurement",
            "definition": "DeviceObservations generated for this DeviceMetric are measured.",
            "display": "Measurement",
        }
    )
    """
    Measurement

    DeviceObservations generated for this DeviceMetric are measured.
    """

    setting = CodeSystemConcept(
        {
            "code": "setting",
            "definition": "DeviceObservations generated for this DeviceMetric is a setting that will influence the behavior of the Device.",
            "display": "Setting",
        }
    )
    """
    Setting

    DeviceObservations generated for this DeviceMetric is a setting that will influence the behavior of the Device.
    """

    calculation = CodeSystemConcept(
        {
            "code": "calculation",
            "definition": "DeviceObservations generated for this DeviceMetric are calculated.",
            "display": "Calculation",
        }
    )
    """
    Calculation

    DeviceObservations generated for this DeviceMetric are calculated.
    """

    unspecified = CodeSystemConcept(
        {
            "code": "unspecified",
            "definition": "The category of this DeviceMetric is unspecified.",
            "display": "Unspecified",
        }
    )
    """
    Unspecified

    The category of this DeviceMetric is unspecified.
    """

    class Meta:
        resource = _resource
