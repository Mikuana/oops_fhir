from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ImmunizationEvaluationDoseStatusReasonCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationEvaluationDoseStatusReasonCodes:
    """
    Immunization Evaluation Dose Status Reason codes

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the reason why an administered dose has
been assigned a particular status. Often, this reason describes why a
dose is considered invalid. This value set is provided as a suggestive
example.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status-reason
    """

    advstorage = CodeSystemConcept(
        {
            "code": "advstorage",
            "definition": "The product was stored in a manner inconsistent with manufacturer guidelines potentially reducing the effectiveness of the product.",
            "display": "Adverse storage condition",
        }
    )
    """
    Adverse storage condition

    The product was stored in a manner inconsistent with manufacturer guidelines potentially reducing the effectiveness of the product.
    """

    coldchbrk = CodeSystemConcept(
        {
            "code": "coldchbrk",
            "definition": "The product was stored at a temperature inconsistent with manufacturer guidelines potentially reducing the effectiveness of the product.",
            "display": "Cold chain break",
        }
    )
    """
    Cold chain break

    The product was stored at a temperature inconsistent with manufacturer guidelines potentially reducing the effectiveness of the product.
    """

    explot = CodeSystemConcept(
        {
            "code": "explot",
            "definition": "The product was administered after the expiration date associated with lot of vaccine.",
            "display": "Expired lot",
        }
    )
    """
    Expired lot

    The product was administered after the expiration date associated with lot of vaccine.
    """

    outsidesched = CodeSystemConcept(
        {
            "code": "outsidesched",
            "definition": "The product was administered at a time inconsistent with the documented schedule.",
            "display": "Administered outside recommended schedule",
        }
    )
    """
    Administered outside recommended schedule

    The product was administered at a time inconsistent with the documented schedule.
    """

    prodrecall = CodeSystemConcept(
        {
            "code": "prodrecall",
            "definition": "The product administered has been recalled by the manufacturer.",
            "display": "Product recall",
        }
    )
    """
    Product recall

    The product administered has been recalled by the manufacturer.
    """

    class Meta:
        resource = _resource
