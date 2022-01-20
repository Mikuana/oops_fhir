from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["BenefitTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class BenefitTypeCodes:
    """
    Benefit Type Codes

    This value set includes a smattering of Benefit type codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/benefit-type
    """

    benefit = CodeSystemConcept(
        {
            "code": "benefit",
            "definition": "Maximum benefit allowable.",
            "display": "Benefit",
        }
    )
    """
    Benefit

    Maximum benefit allowable.
    """

    deductible = CodeSystemConcept(
        {
            "code": "deductible",
            "definition": "Cost to be incurred before benefits are applied",
            "display": "Deductible",
        }
    )
    """
    Deductible

    Cost to be incurred before benefits are applied
    """

    visit = CodeSystemConcept(
        {"code": "visit", "definition": "Service visit", "display": "Visit"}
    )
    """
    Visit

    Service visit
    """

    room = CodeSystemConcept(
        {"code": "room", "definition": "Type of room", "display": "Room"}
    )
    """
    Room

    Type of room
    """

    copay = CodeSystemConcept(
        {
            "code": "copay",
            "definition": "Copayment per service",
            "display": "Copayment per service",
        }
    )
    """
    Copayment per service

    Copayment per service
    """

    copay_percent = CodeSystemConcept(
        {
            "code": "copay-percent",
            "definition": "Copayment percentage per service",
            "display": "Copayment Percent per service",
        }
    )
    """
    Copayment Percent per service

    Copayment percentage per service
    """

    copay_maximum = CodeSystemConcept(
        {
            "code": "copay-maximum",
            "definition": "Copayment maximum per service",
            "display": "Copayment maximum per service",
        }
    )
    """
    Copayment maximum per service

    Copayment maximum per service
    """

    vision_exam = CodeSystemConcept(
        {"code": "vision-exam", "definition": "Vision Exam", "display": "Vision Exam"}
    )
    """
    Vision Exam

    Vision Exam
    """

    vision_glasses = CodeSystemConcept(
        {
            "code": "vision-glasses",
            "definition": "Frames and lenses",
            "display": "Vision Glasses",
        }
    )
    """
    Vision Glasses

    Frames and lenses
    """

    vision_contacts = CodeSystemConcept(
        {
            "code": "vision-contacts",
            "definition": "Contact Lenses",
            "display": "Vision Contacts Coverage",
        }
    )
    """
    Vision Contacts Coverage

    Contact Lenses
    """

    medical_primarycare = CodeSystemConcept(
        {
            "code": "medical-primarycare",
            "definition": "Medical Primary Health Coverage",
            "display": "Medical Primary Health Coverage",
        }
    )
    """
    Medical Primary Health Coverage

    Medical Primary Health Coverage
    """

    pharmacy_dispense = CodeSystemConcept(
        {
            "code": "pharmacy-dispense",
            "definition": "Pharmacy Dispense Coverage",
            "display": "Pharmacy Dispense Coverage",
        }
    )
    """
    Pharmacy Dispense Coverage

    Pharmacy Dispense Coverage
    """

    class Meta:
        resource = _resource
