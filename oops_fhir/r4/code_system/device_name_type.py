from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DeviceNameType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DeviceNameType:
    """
    DeviceNameType

    The type of name the device is referred by.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/device-nametype
    """

    udi_label_name = CodeSystemConcept(
        {
            "code": "udi-label-name",
            "definition": "UDI Label name.",
            "display": "UDI Label name",
        }
    )
    """
    UDI Label name

    UDI Label name.
    """

    user_friendly_name = CodeSystemConcept(
        {
            "code": "user-friendly-name",
            "definition": "User Friendly name.",
            "display": "User Friendly name",
        }
    )
    """
    User Friendly name

    User Friendly name.
    """

    patient_reported_name = CodeSystemConcept(
        {
            "code": "patient-reported-name",
            "definition": "Patient Reported name.",
            "display": "Patient Reported name",
        }
    )
    """
    Patient Reported name

    Patient Reported name.
    """

    manufacturer_name = CodeSystemConcept(
        {
            "code": "manufacturer-name",
            "definition": "Manufacturer name.",
            "display": "Manufacturer name",
        }
    )
    """
    Manufacturer name

    Manufacturer name.
    """

    model_name = CodeSystemConcept(
        {"code": "model-name", "definition": "Model name.", "display": "Model name"}
    )
    """
    Model name

    Model name.
    """

    other = CodeSystemConcept(
        {"code": "other", "definition": "other.", "display": "other"}
    )
    """
    other

    other.
    """

    class Meta:
        resource = _resource
