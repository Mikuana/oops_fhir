from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["FHIRDeviceStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class FHIRDeviceStatus:
    """
    FHIRDeviceStatus

    The availability status of the device.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/device-status
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "The device is available for use.  Note: For *implanted devices*  this means that the device is implanted in the patient.",
            "display": "Active",
        }
    )
    """
    Active

    The device is available for use.  Note: For *implanted devices*  this means that the device is implanted in the patient.
    """

    inactive = CodeSystemConcept(
        {
            "code": "inactive",
            "definition": "The device is no longer available for use (e.g. lost, expired, damaged).  Note: For *implanted devices*  this means that the device has been removed from the patient.",
            "display": "Inactive",
        }
    )
    """
    Inactive

    The device is no longer available for use (e.g. lost, expired, damaged).  Note: For *implanted devices*  this means that the device has been removed from the patient.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The device was entered in error and voided.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The device was entered in error and voided.
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": "The status of the device has not been determined.",
            "display": "Unknown",
        }
    )
    """
    Unknown

    The status of the device has not been determined.
    """

    class Meta:
        resource = _resource
