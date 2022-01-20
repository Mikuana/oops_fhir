from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["Program"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class Program:
    """
    Program

    This value set defines an example set of codes that could be can be used
to classify groupings of service-types/specialties.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/program
    """

    one = CodeSystemConcept(
        {"code": "1", "display": "Acquired Brain Injury (ABI) Program\xa0"}
    )
    """
    Acquired Brain Injury (ABI) Program 

    
    """

    two = CodeSystemConcept(
        {"code": "2", "display": "ABI Slow To Recover (ABI STR) Program"}
    )
    """
    ABI Slow To Recover (ABI STR) Program

    
    """

    three = CodeSystemConcept({"code": "3", "display": "Access Programs"})
    """
    Access Programs

    
    """

    four = CodeSystemConcept(
        {"code": "4", "display": "Adult and Further Education (ACFE) Program"}
    )
    """
    Adult and Further Education (ACFE) Program

    
    """

    five = CodeSystemConcept(
        {
            "code": "5",
            "display": "Adult Day Activity and Support Services (ADASS) Program",
        }
    )
    """
    Adult Day Activity and Support Services (ADASS) Program

    
    """

    six = CodeSystemConcept({"code": "6", "display": "Adult Day Care Program"})
    """
    Adult Day Care Program

    
    """

    seven = CodeSystemConcept(
        {"code": "7", "display": "ATSS (Adult Training Support Service)"}
    )
    """
    ATSS (Adult Training Support Service)

    
    """

    eight = CodeSystemConcept(
        {"code": "8", "display": "Community Aged Care Packages (CACP)"}
    )
    """
    Community Aged Care Packages (CACP)

    
    """

    nine = CodeSystemConcept(
        {"code": "9", "display": "Care Coordination & Supplementary Services (CCSS)"}
    )
    """
    Care Coordination & Supplementary Services (CCSS)

    
    """

    one0 = CodeSystemConcept(
        {"code": "10", "display": "Cognitive Dementia Memory Service (CDAMS)"}
    )
    """
    Cognitive Dementia Memory Service (CDAMS)

    
    """

    one1 = CodeSystemConcept({"code": "11", "display": "ChildFIRST"})
    """
    ChildFIRST

    
    """

    one2 = CodeSystemConcept({"code": "12", "display": "Children's Contact Services"})
    """
    Children's Contact Services

    
    """

    one3 = CodeSystemConcept({"code": "13", "display": "Community Visitors Scheme"})
    """
    Community Visitors Scheme

    
    """

    one4 = CodeSystemConcept(
        {"code": "14", "display": "CPP (Community Partners Program)"}
    )
    """
    CPP (Community Partners Program)

    
    """

    one5 = CodeSystemConcept({"code": "15", "display": "Closing the Gap (CTG)"})
    """
    Closing the Gap (CTG)

    
    """

    one6 = CodeSystemConcept(
        {"code": "16", "display": "Coordinated Veterans' Care (CVC) Program"}
    )
    """
    Coordinated Veterans' Care (CVC) Program

    
    """

    one7 = CodeSystemConcept({"code": "17", "display": "Day Program"})
    """
    Day Program

    
    """

    one8 = CodeSystemConcept({"code": "18", "display": "Drop In Program"})
    """
    Drop In Program

    
    """

    one9 = CodeSystemConcept({"code": "19", "display": "Early Years Program"})
    """
    Early Years Program

    
    """

    two0 = CodeSystemConcept({"code": "20", "display": "Employee Assistance Program"})
    """
    Employee Assistance Program

    
    """

    two1 = CodeSystemConcept(
        {"code": "21", "display": "Home And Community Care (HACC)"}
    )
    """
    Home And Community Care (HACC)

    
    """

    two2 = CodeSystemConcept(
        {"code": "22", "display": "Hospital Admission Risk Program (HARP)"}
    )
    """
    Hospital Admission Risk Program (HARP)

    
    """

    two3 = CodeSystemConcept(
        {"code": "23", "display": "Hospital in the Home (HITH) Program"}
    )
    """
    Hospital in the Home (HITH) Program

    
    """

    two4 = CodeSystemConcept(
        {"code": "24", "display": "ICTP (Intensive Community Treatment Program)"}
    )
    """
    ICTP (Intensive Community Treatment Program)

    
    """

    two5 = CodeSystemConcept(
        {"code": "25", "display": "IFSS (Intensive Family Support Program)"}
    )
    """
    IFSS (Intensive Family Support Program)

    
    """

    two6 = CodeSystemConcept(
        {"code": "26", "display": "JPET (Job Placement, Education and Training)"}
    )
    """
    JPET (Job Placement, Education and Training)

    
    """

    two7 = CodeSystemConcept(
        {"code": "27", "display": "Koori Juvenile Justice Program"}
    )
    """
    Koori Juvenile Justice Program

    
    """

    two8 = CodeSystemConcept(
        {"code": "28", "display": "Language Literacy and Numeracy Program"}
    )
    """
    Language Literacy and Numeracy Program

    
    """

    two9 = CodeSystemConcept({"code": "29", "display": "Life Skills Program"})
    """
    Life Skills Program

    
    """

    three0 = CodeSystemConcept(
        {"code": "30", "display": "LMP (Lifestyle Modification Program)"}
    )
    """
    LMP (Lifestyle Modification Program)

    
    """

    three1 = CodeSystemConcept({"code": "31", "display": "MedsCheck Program"})
    """
    MedsCheck Program

    
    """

    three2 = CodeSystemConcept(
        {"code": "32", "display": "Methadone/Buprenorphine Program"}
    )
    """
    Methadone/Buprenorphine Program

    
    """

    three3 = CodeSystemConcept(
        {"code": "33", "display": "National Disabilities Insurance Scheme (NDIS)"}
    )
    """
    National Disabilities Insurance Scheme (NDIS)

    
    """

    three4 = CodeSystemConcept(
        {"code": "34", "display": "National Diabetes Services Scheme (NDSS)"}
    )
    """
    National Diabetes Services Scheme (NDSS)

    
    """

    three5 = CodeSystemConcept({"code": "35", "display": "Needle/Syringe Program"})
    """
    Needle/Syringe Program

    
    """

    three6 = CodeSystemConcept({"code": "36", "display": "nPEP Program"})
    """
    nPEP Program

    
    """

    three7 = CodeSystemConcept({"code": "37", "display": "Personal Support Program"})
    """
    Personal Support Program

    
    """

    three8 = CodeSystemConcept(
        {"code": "38", "display": "Partners in Recovery (PIR) Program"}
    )
    """
    Partners in Recovery (PIR) Program

    
    """

    three9 = CodeSystemConcept({"code": "39", "display": "Pre-employment Program"})
    """
    Pre-employment Program

    
    """

    four0 = CodeSystemConcept({"code": "40", "display": "Reconnect Program"})
    """
    Reconnect Program

    
    """

    four1 = CodeSystemConcept(
        {
            "code": "41",
            "display": "Sexual Abuse Counselling and Prevention Program (SACPP)",
        }
    )
    """
    Sexual Abuse Counselling and Prevention Program (SACPP)

    
    """

    four2 = CodeSystemConcept({"code": "42", "display": "Social Support Programs"})
    """
    Social Support Programs

    
    """

    four3 = CodeSystemConcept(
        {"code": "43", "display": "Supported Residential Service (SRS)"}
    )
    """
    Supported Residential Service (SRS)

    
    """

    four4 = CodeSystemConcept(
        {"code": "44", "display": "Tasmanian Aboriginal Centre (TAC)"}
    )
    """
    Tasmanian Aboriginal Centre (TAC)

    
    """

    four5 = CodeSystemConcept({"code": "45", "display": "Victim's Assistance Program"})
    """
    Victim's Assistance Program

    
    """

    class Meta:
        resource = _resource
