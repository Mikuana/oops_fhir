from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DeviceMetricCalibrationState"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DeviceMetricCalibrationState:
    """
    DeviceMetricCalibrationState

    Describes the state of a metric calibration.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/metric-calibration-state
    """

    not_calibrated = CodeSystemConcept(
        {
            "code": "not-calibrated",
            "definition": "The metric has not been calibrated.",
            "display": "Not Calibrated",
        }
    )
    """
    Not Calibrated

    The metric has not been calibrated.
    """

    calibration_required = CodeSystemConcept(
        {
            "code": "calibration-required",
            "definition": "The metric needs to be calibrated.",
            "display": "Calibration Required",
        }
    )
    """
    Calibration Required

    The metric needs to be calibrated.
    """

    calibrated = CodeSystemConcept(
        {
            "code": "calibrated",
            "definition": "The metric has been calibrated.",
            "display": "Calibrated",
        }
    )
    """
    Calibrated

    The metric has been calibrated.
    """

    unspecified = CodeSystemConcept(
        {
            "code": "unspecified",
            "definition": "The state of calibration of this metric is unspecified.",
            "display": "Unspecified",
        }
    )
    """
    Unspecified

    The state of calibration of this metric is unspecified.
    """

    class Meta:
        resource = _resource
