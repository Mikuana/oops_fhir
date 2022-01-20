from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CatalogType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CatalogType:
    """
    CatalogType

    The type of catalog.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/catalogType
    """

    medication = CodeSystemConcept(
        {
            "code": "medication",
            "definition": "Medication Catalog.",
            "display": "Medication Catalog",
        }
    )
    """
    Medication Catalog

    Medication Catalog.
    """

    device = CodeSystemConcept(
        {"code": "device", "definition": "Device Catalog.", "display": "Device Catalog"}
    )
    """
    Device Catalog

    Device Catalog.
    """

    protocol = CodeSystemConcept(
        {"code": "protocol", "definition": "Protocol List.", "display": "Protocol List"}
    )
    """
    Protocol List

    Protocol List.
    """

    class Meta:
        resource = _resource
