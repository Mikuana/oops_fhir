from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["BenefitCategoryCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class BenefitCategoryCodes:
    """
    Benefit Category Codes

    This value set includes examples of Benefit Category codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/ex-benefitcategory
    """

    one = CodeSystemConcept(
        {"code": "1", "definition": "Medical Care.", "display": "Medical Care"}
    )
    """
    Medical Care

    Medical Care.
    """

    two = CodeSystemConcept(
        {"code": "2", "definition": "Surgical.", "display": "Surgical"}
    )
    """
    Surgical

    Surgical.
    """

    three = CodeSystemConcept(
        {"code": "3", "definition": "Consultation.", "display": "Consultation"}
    )
    """
    Consultation

    Consultation.
    """

    four = CodeSystemConcept(
        {"code": "4", "definition": "Diagnostic XRay.", "display": "Diagnostic XRay"}
    )
    """
    Diagnostic XRay

    Diagnostic XRay.
    """

    five = CodeSystemConcept(
        {"code": "5", "definition": "Diagnostic Lab.", "display": "Diagnostic Lab"}
    )
    """
    Diagnostic Lab

    Diagnostic Lab.
    """

    one4 = CodeSystemConcept(
        {
            "code": "14",
            "definition": "Renal Supplies excluding Dialysis.",
            "display": "Renal Supplies",
        }
    )
    """
    Renal Supplies

    Renal Supplies excluding Dialysis.
    """

    two3 = CodeSystemConcept(
        {
            "code": "23",
            "definition": "Diagnostic Dental.",
            "display": "Diagnostic Dental",
        }
    )
    """
    Diagnostic Dental

    Diagnostic Dental.
    """

    two4 = CodeSystemConcept(
        {"code": "24", "definition": "Periodontics.", "display": "Periodontics"}
    )
    """
    Periodontics

    Periodontics.
    """

    two5 = CodeSystemConcept(
        {"code": "25", "definition": "Restorative.", "display": "Restorative"}
    )
    """
    Restorative

    Restorative.
    """

    two6 = CodeSystemConcept(
        {"code": "26", "definition": "Endodontics.", "display": "Endodontics"}
    )
    """
    Endodontics

    Endodontics.
    """

    two7 = CodeSystemConcept(
        {
            "code": "27",
            "definition": "Maxillofacial Prosthetics.",
            "display": "Maxillofacial Prosthetics",
        }
    )
    """
    Maxillofacial Prosthetics

    Maxillofacial Prosthetics.
    """

    two8 = CodeSystemConcept(
        {
            "code": "28",
            "definition": "Adjunctive Dental Services.",
            "display": "Adjunctive Dental Services",
        }
    )
    """
    Adjunctive Dental Services

    Adjunctive Dental Services.
    """

    three0 = CodeSystemConcept(
        {
            "code": "30",
            "definition": "Health Benefit Plan Coverage.",
            "display": "Health Benefit Plan Coverage",
        }
    )
    """
    Health Benefit Plan Coverage

    Health Benefit Plan Coverage.
    """

    three5 = CodeSystemConcept(
        {"code": "35", "definition": "Dental Care.", "display": "Dental Care"}
    )
    """
    Dental Care

    Dental Care.
    """

    three6 = CodeSystemConcept(
        {"code": "36", "definition": "Dental Crowns.", "display": "Dental Crowns"}
    )
    """
    Dental Crowns

    Dental Crowns.
    """

    three7 = CodeSystemConcept(
        {"code": "37", "definition": "Dental Accident.", "display": "Dental Accident"}
    )
    """
    Dental Accident

    Dental Accident.
    """

    four9 = CodeSystemConcept(
        {
            "code": "49",
            "definition": "Hospital Room and Board.",
            "display": "Hospital Room and Board",
        }
    )
    """
    Hospital Room and Board

    Hospital Room and Board.
    """

    five5 = CodeSystemConcept(
        {"code": "55", "definition": "Major Medical.", "display": "Major Medical"}
    )
    """
    Major Medical

    Major Medical.
    """

    five6 = CodeSystemConcept(
        {
            "code": "56",
            "definition": "Medically Related Transportation.",
            "display": "Medically Related Transportation",
        }
    )
    """
    Medically Related Transportation

    Medically Related Transportation.
    """

    six1 = CodeSystemConcept(
        {
            "code": "61",
            "definition": "In-vitro Fertilization.",
            "display": "In-vitro Fertilization",
        }
    )
    """
    In-vitro Fertilization

    In-vitro Fertilization.
    """

    six2 = CodeSystemConcept(
        {"code": "62", "definition": "MRI Scan.", "display": "MRI Scan"}
    )
    """
    MRI Scan

    MRI Scan.
    """

    six3 = CodeSystemConcept(
        {
            "code": "63",
            "definition": "Donor Procedures such as organ harvest.",
            "display": "Donor Procedures",
        }
    )
    """
    Donor Procedures

    Donor Procedures such as organ harvest.
    """

    six9 = CodeSystemConcept(
        {"code": "69", "definition": "Maternity.", "display": "Maternity"}
    )
    """
    Maternity

    Maternity.
    """

    seven6 = CodeSystemConcept(
        {"code": "76", "definition": "Renal dialysis.", "display": "Renal Dialysis"}
    )
    """
    Renal Dialysis

    Renal dialysis.
    """

    f1 = CodeSystemConcept(
        {"code": "F1", "definition": "Medical Coverage.", "display": "Medical Coverage"}
    )
    """
    Medical Coverage

    Medical Coverage.
    """

    f3 = CodeSystemConcept(
        {"code": "F3", "definition": "Dental Coverage.", "display": "Dental Coverage"}
    )
    """
    Dental Coverage

    Dental Coverage.
    """

    f4 = CodeSystemConcept(
        {"code": "F4", "definition": "Hearing Coverage.", "display": "Hearing Coverage"}
    )
    """
    Hearing Coverage

    Hearing Coverage.
    """

    f6 = CodeSystemConcept(
        {"code": "F6", "definition": "Vision Coverage.", "display": "Vision Coverage"}
    )
    """
    Vision Coverage

    Vision Coverage.
    """

    class Meta:
        resource = _resource
