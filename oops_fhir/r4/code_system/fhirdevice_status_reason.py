from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["FHIRDeviceStatusReason"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class FHIRDeviceStatusReason:
    """
    FHIRDeviceStatusReason

    The availability status reason of the device.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/device-status-reason
    """

    online = CodeSystemConcept(
        {"code": "online", "definition": "The device is off.", "display": "Online"}
    )
    """
    Online

    The device is off.
    """

    paused = CodeSystemConcept(
        {"code": "paused", "definition": "The device is paused.", "display": "Paused"}
    )
    """
    Paused

    The device is paused.
    """

    standby = CodeSystemConcept(
        {
            "code": "standby",
            "definition": "The device is ready but not actively operating.",
            "display": "Standby",
        }
    )
    """
    Standby

    The device is ready but not actively operating.
    """

    offline = CodeSystemConcept(
        {
            "code": "offline",
            "definition": "The device is offline.",
            "display": "Offline",
        }
    )
    """
    Offline

    The device is offline.
    """

    not_ready = CodeSystemConcept(
        {
            "code": "not-ready",
            "definition": "The device is not ready.",
            "display": "Not Ready",
        }
    )
    """
    Not Ready

    The device is not ready.
    """

    transduc_discon = CodeSystemConcept(
        {
            "code": "transduc-discon",
            "definition": "The device transducer is disconnected.",
            "display": "Transducer Disconnected",
        }
    )
    """
    Transducer Disconnected

    The device transducer is disconnected.
    """

    hw_discon = CodeSystemConcept(
        {
            "code": "hw-discon",
            "definition": "The device hardware is disconnected.",
            "display": "Hardware Disconnected",
        }
    )
    """
    Hardware Disconnected

    The device hardware is disconnected.
    """

    off = CodeSystemConcept(
        {"code": "off", "definition": "The device is off.", "display": "Off"}
    )
    """
    Off

    The device is off.
    """

    class Meta:
        resource = _resource
