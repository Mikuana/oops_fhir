from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SupplyItemType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SupplyItemType:
    """
    Supply Item Type

    This value sets refers to a specific supply item.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/supply-item-type
    """

    medication = CodeSystemConcept(
        {
            "code": "medication",
            "definition": "Supply is a kind of medication.",
            "display": "Medication",
        }
    )
    """
    Medication

    Supply is a kind of medication.
    """

    device = CodeSystemConcept(
        {
            "code": "device",
            "definition": "What is supplied (or requested) is a device.",
            "display": "Device",
        }
    )
    """
    Device

    What is supplied (or requested) is a device.
    """

    class Meta:
        resource = _resource
