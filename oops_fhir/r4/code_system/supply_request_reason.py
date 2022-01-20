from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SupplyRequestReason"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SupplyRequestReason:
    """
    SupplyRequestReason

    The reason why the supply item was requested.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/supplyrequest-reason
    """

    patient_care = CodeSystemConcept(
        {
            "code": "patient-care",
            "definition": "The supply has been requested for use in direct patient care.",
            "display": "Patient Care",
        }
    )
    """
    Patient Care

    The supply has been requested for use in direct patient care.
    """

    ward_stock = CodeSystemConcept(
        {
            "code": "ward-stock",
            "definition": "The supply has been requested for creating or replenishing ward stock.",
            "display": "Ward Stock",
        }
    )
    """
    Ward Stock

    The supply has been requested for creating or replenishing ward stock.
    """

    class Meta:
        resource = _resource
