from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DeviceMetricCalibrationType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DeviceMetricCalibrationType:
    """
    DeviceMetricCalibrationType

    Describes the type of a metric calibration.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/metric-calibration-type
    """

    unspecified = CodeSystemConcept(
        {
            "code": "unspecified",
            "definition": "Metric calibration method has not been identified.",
            "display": "Unspecified",
        }
    )
    """
    Unspecified

    Metric calibration method has not been identified.
    """

    offset = CodeSystemConcept(
        {
            "code": "offset",
            "definition": "Offset metric calibration method.",
            "display": "Offset",
        }
    )
    """
    Offset

    Offset metric calibration method.
    """

    gain = CodeSystemConcept(
        {
            "code": "gain",
            "definition": "Gain metric calibration method.",
            "display": "Gain",
        }
    )
    """
    Gain

    Gain metric calibration method.
    """

    two_point = CodeSystemConcept(
        {
            "code": "two-point",
            "definition": "Two-point metric calibration method.",
            "display": "Two Point",
        }
    )
    """
    Two Point

    Two-point metric calibration method.
    """

    class Meta:
        resource = _resource
