from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DeviceMetricOperationalStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DeviceMetricOperationalStatus:
    """
    DeviceMetricOperationalStatus

    Describes the operational status of the DeviceMetric.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/metric-operational-status
    """

    on = CodeSystemConcept(
        {
            "code": "on",
            "definition": "The DeviceMetric is operating and will generate DeviceObservations.",
            "display": "On",
        }
    )
    """
    On

    The DeviceMetric is operating and will generate DeviceObservations.
    """

    off = CodeSystemConcept(
        {
            "code": "off",
            "definition": "The DeviceMetric is not operating.",
            "display": "Off",
        }
    )
    """
    Off

    The DeviceMetric is not operating.
    """

    standby = CodeSystemConcept(
        {
            "code": "standby",
            "definition": "The DeviceMetric is operating, but will not generate any DeviceObservations.",
            "display": "Standby",
        }
    )
    """
    Standby

    The DeviceMetric is operating, but will not generate any DeviceObservations.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The DeviceMetric was entered in error.",
            "display": "Entered In Error",
        }
    )
    """
    Entered In Error

    The DeviceMetric was entered in error.
    """

    class Meta:
        resource = _resource
