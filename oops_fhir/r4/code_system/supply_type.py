from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SupplyType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SupplyType:
    """
    Supply Type

    This value sets refers to a Category of supply.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/supply-kind
    """

    central = CodeSystemConcept(
        {
            "code": "central",
            "definition": "Supply is stored and requested from central supply.",
            "display": "Central Supply",
        }
    )
    """
    Central Supply

    Supply is stored and requested from central supply.
    """

    nonstock = CodeSystemConcept(
        {
            "code": "nonstock",
            "definition": "Supply is not onsite and must be requested from an outside vendor using a non-stock requisition.",
            "display": "Non-Stock",
        }
    )
    """
    Non-Stock

    Supply is not onsite and must be requested from an outside vendor using a non-stock requisition.
    """

    class Meta:
        resource = _resource
