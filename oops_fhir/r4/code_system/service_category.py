from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ServiceCategory"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ServiceCategory:
    """
    Service category

    This value set defines an example set of codes that can be used to
classify groupings of service-types/specialties.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/service-category
    """

    one = CodeSystemConcept(
        {"code": "1", "definition": "Adoption", "display": "Adoption"}
    )
    """
    Adoption

    Adoption
    """

    two = CodeSystemConcept(
        {"code": "2", "definition": "Aged Care", "display": "Aged Care"}
    )
    """
    Aged Care

    Aged Care
    """

    three4 = CodeSystemConcept(
        {"code": "34", "definition": "Allied Health", "display": "Allied Health"}
    )
    """
    Allied Health

    Allied Health
    """

    three = CodeSystemConcept(
        {
            "code": "3",
            "definition": "Alternative & Complementary Therapies",
            "display": "Alternative/Complementary Therapies",
        }
    )
    """
    Alternative/Complementary Therapies

    Alternative & Complementary Therapies
    """

    four = CodeSystemConcept(
        {
            "code": "4",
            "definition": "Child Care and/or Kindergarten",
            "display": "Child Care /Kindergarten",
        }
    )
    """
    Child Care /Kindergarten

    Child Care and/or Kindergarten
    """

    five = CodeSystemConcept(
        {"code": "5", "definition": "Child Development", "display": "Child Development"}
    )
    """
    Child Development

    Child Development
    """

    six = CodeSystemConcept(
        {
            "code": "6",
            "definition": "Child Protection & Family Services",
            "display": "Child Protection & Family Services",
        }
    )
    """
    Child Protection & Family Services

    Child Protection & Family Services
    """

    seven = CodeSystemConcept(
        {
            "code": "7",
            "definition": "Community Health Care",
            "display": "Community Health Care",
        }
    )
    """
    Community Health Care

    Community Health Care
    """

    eight = CodeSystemConcept(
        {"code": "8", "definition": "Counselling", "display": "Counselling"}
    )
    """
    Counselling

    Counselling
    """

    three6 = CodeSystemConcept(
        {
            "code": "36",
            "definition": "Crisis Line (GPAH use only)",
            "display": "Crisis Line (GPAH use only)",
        }
    )
    """
    Crisis Line (GPAH use only)

    Crisis Line (GPAH use only)
    """

    nine = CodeSystemConcept(
        {"code": "9", "definition": "Death Services", "display": "Death Services"}
    )
    """
    Death Services

    Death Services
    """

    one0 = CodeSystemConcept(
        {"code": "10", "definition": "Dental", "display": "Dental"}
    )
    """
    Dental

    Dental
    """

    one1 = CodeSystemConcept(
        {
            "code": "11",
            "definition": "Disability Support",
            "display": "Disability Support",
        }
    )
    """
    Disability Support

    Disability Support
    """

    one2 = CodeSystemConcept(
        {"code": "12", "definition": "Drug/Alcohol", "display": "Drug/Alcohol"}
    )
    """
    Drug/Alcohol

    Drug/Alcohol
    """

    one3 = CodeSystemConcept(
        {
            "code": "13",
            "definition": "Education & Learning",
            "display": "Education & Learning",
        }
    )
    """
    Education & Learning

    Education & Learning
    """

    one4 = CodeSystemConcept(
        {
            "code": "14",
            "definition": "Emergency Department",
            "display": "Emergency Department",
        }
    )
    """
    Emergency Department

    Emergency Department
    """

    one5 = CodeSystemConcept(
        {"code": "15", "definition": "Employment", "display": "Employment"}
    )
    """
    Employment

    Employment
    """

    one6 = CodeSystemConcept(
        {
            "code": "16",
            "definition": "Financial & Material aid",
            "display": "Financial & Material Aid",
        }
    )
    """
    Financial & Material Aid

    Financial & Material aid
    """

    one7 = CodeSystemConcept(
        {
            "code": "17",
            "definition": "General Practice/GP (doctor)",
            "display": "General Practice",
        }
    )
    """
    General Practice

    General Practice/GP (doctor)
    """

    three5 = CodeSystemConcept(
        {"code": "35", "definition": "Hospital", "display": "Hospital"}
    )
    """
    Hospital

    Hospital
    """

    one8 = CodeSystemConcept(
        {
            "code": "18",
            "definition": "Housing/Homelessness",
            "display": "Housing/Homelessness",
        }
    )
    """
    Housing/Homelessness

    Housing/Homelessness
    """

    one9 = CodeSystemConcept(
        {"code": "19", "definition": "Interpreting", "display": "Interpreting"}
    )
    """
    Interpreting

    Interpreting
    """

    two0 = CodeSystemConcept(
        {"code": "20", "definition": "Justice", "display": "Justice"}
    )
    """
    Justice

    Justice
    """

    two1 = CodeSystemConcept({"code": "21", "definition": "Legal", "display": "Legal"})
    """
    Legal

    Legal
    """

    two2 = CodeSystemConcept(
        {"code": "22", "definition": "Mental Health", "display": "Mental Health"}
    )
    """
    Mental Health

    Mental Health
    """

    three8 = CodeSystemConcept({"code": "38", "definition": "NDIA", "display": "NDIA"})
    """
    NDIA

    NDIA
    """

    two3 = CodeSystemConcept(
        {
            "code": "23",
            "definition": "Physical Activity & Recreation",
            "display": "Physical Activity & Recreation",
        }
    )
    """
    Physical Activity & Recreation

    Physical Activity & Recreation
    """

    two4 = CodeSystemConcept(
        {"code": "24", "definition": "Regulation", "display": "Regulation"}
    )
    """
    Regulation

    Regulation
    """

    two5 = CodeSystemConcept(
        {
            "code": "25",
            "definition": "Respite/Carer Support",
            "display": "Respite/Carer Support",
        }
    )
    """
    Respite/Carer Support

    Respite/Carer Support
    """

    two6 = CodeSystemConcept(
        {
            "code": "26",
            "definition": "Specialist Clinical Pathology - requires referral",
            "display": "Specialist Clinical Pathology",
        }
    )
    """
    Specialist Clinical Pathology

    Specialist Clinical Pathology - requires referral
    """

    two7 = CodeSystemConcept(
        {
            "code": "27",
            "definition": "Specialist Medical - requires referral",
            "display": "Specialist Medical",
        }
    )
    """
    Specialist Medical

    Specialist Medical - requires referral
    """

    two8 = CodeSystemConcept(
        {
            "code": "28",
            "definition": "Specialist Obstetrics & Gynecology - requires referral",
            "display": "Specialist Obstetrics & Gynecology",
        }
    )
    """
    Specialist Obstetrics & Gynecology

    Specialist Obstetrics & Gynecology - requires referral
    """

    two9 = CodeSystemConcept(
        {
            "code": "29",
            "definition": "Specialist Paediatric - requires referral",
            "display": "Specialist Paediatric",
        }
    )
    """
    Specialist Paediatric

    Specialist Paediatric - requires referral
    """

    three0 = CodeSystemConcept(
        {
            "code": "30",
            "definition": "Specialist Radiology/Imaging - requires referral",
            "display": "Specialist Radiology/Imaging",
        }
    )
    """
    Specialist Radiology/Imaging

    Specialist Radiology/Imaging - requires referral
    """

    three1 = CodeSystemConcept(
        {
            "code": "31",
            "definition": "Specialist Surgical - requires referral",
            "display": "Specialist Surgical",
        }
    )
    """
    Specialist Surgical

    Specialist Surgical - requires referral
    """

    three2 = CodeSystemConcept(
        {"code": "32", "definition": "Support group/s", "display": "Support Group/s"}
    )
    """
    Support Group/s

    Support group/s
    """

    three7 = CodeSystemConcept(
        {
            "code": "37",
            "definition": "Test Message (HSD admin use only)",
            "display": "Test Message (HSD admin)",
        }
    )
    """
    Test Message (HSD admin)

    Test Message (HSD admin use only)
    """

    three3 = CodeSystemConcept(
        {"code": "33", "definition": "Transport", "display": "Transport"}
    )
    """
    Transport

    Transport
    """

    class Meta:
        resource = _resource
