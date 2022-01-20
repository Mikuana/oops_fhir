from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContactEntityType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContactEntityType:
    """
    Contact entity type

    This example value set defines a set of codes that can be used to
indicate the purpose for which you would contact a contact party.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/contactentity-type
    """

    bill = CodeSystemConcept(
        {
            "code": "BILL",
            "definition": "Contact details for information regarding to billing/general finance enquiries.",
            "display": "Billing",
        }
    )
    """
    Billing

    Contact details for information regarding to billing/general finance enquiries.
    """

    admin = CodeSystemConcept(
        {
            "code": "ADMIN",
            "definition": "Contact details for administrative enquiries.",
            "display": "Administrative",
        }
    )
    """
    Administrative

    Contact details for administrative enquiries.
    """

    hr = CodeSystemConcept(
        {
            "code": "HR",
            "definition": "Contact details for issues related to Human Resources, such as staff matters, OH&S etc.",
            "display": "Human Resource",
        }
    )
    """
    Human Resource

    Contact details for issues related to Human Resources, such as staff matters, OH&S etc.
    """

    payor = CodeSystemConcept(
        {
            "code": "PAYOR",
            "definition": "Contact details for dealing with issues related to insurance claims/adjudication/payment.",
            "display": "Payor",
        }
    )
    """
    Payor

    Contact details for dealing with issues related to insurance claims/adjudication/payment.
    """

    patinf = CodeSystemConcept(
        {
            "code": "PATINF",
            "definition": "Generic information contact for patients.",
            "display": "Patient",
        }
    )
    """
    Patient

    Generic information contact for patients.
    """

    press = CodeSystemConcept(
        {
            "code": "PRESS",
            "definition": "Dedicated contact point for matters relating to press enquiries.",
            "display": "Press",
        }
    )
    """
    Press

    Dedicated contact point for matters relating to press enquiries.
    """

    class Meta:
        resource = _resource
