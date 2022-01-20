from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExampleServicePlaceCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExampleServicePlaceCodes:
    """
    Example Service Place Codes

    This value set includes a smattering of Service Place codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/ex-serviceplace
    """

    zero1 = CodeSystemConcept(
        {
            "code": "01",
            "definition": "A facility or location where drugs and other medically related items and services are sold, dispensed, or otherwise provided directly to patients.",
            "display": "Pharmacy",
        }
    )
    """
    Pharmacy

    A facility or location where drugs and other medically related items and services are sold, dispensed, or otherwise provided directly to patients.
    """

    zero3 = CodeSystemConcept(
        {
            "code": "03",
            "definition": "A facility whose primary purpose is education.",
            "display": "School",
        }
    )
    """
    School

    A facility whose primary purpose is education.
    """

    zero4 = CodeSystemConcept(
        {
            "code": "04",
            "definition": "A facility or location whose primary purpose is to provide temporary housing to homeless individuals (e.g., emergency shelters, individual or family shelters).",
            "display": "Homeless Shelter",
        }
    )
    """
    Homeless Shelter

    A facility or location whose primary purpose is to provide temporary housing to homeless individuals (e.g., emergency shelters, individual or family shelters).
    """

    zero5 = CodeSystemConcept(
        {
            "code": "05",
            "definition": "A facility or location, owned and operated by the Indian Health Service, which provides diagnostic, therapeutic (surgical and nonsurgical), and rehabilitation services to American Indians and Alaska Natives who do not require hospitalization.",
            "display": "Indian Health Service Free-standing Facility",
        }
    )
    """
    Indian Health Service Free-standing Facility

    A facility or location, owned and operated by the Indian Health Service, which provides diagnostic, therapeutic (surgical and nonsurgical), and rehabilitation services to American Indians and Alaska Natives who do not require hospitalization.
    """

    zero6 = CodeSystemConcept(
        {
            "code": "06",
            "definition": "A facility or location, owned and operated by the Indian Health Service, which provides diagnostic, therapeutic (surgical and nonsurgical), and rehabilitation services rendered by, or under the supervision of, physicians to American Indians and Alaska Natives admitted as inpatients or outpatients.",
            "display": "Indian Health Service Provider-based Facility",
        }
    )
    """
    Indian Health Service Provider-based Facility

    A facility or location, owned and operated by the Indian Health Service, which provides diagnostic, therapeutic (surgical and nonsurgical), and rehabilitation services rendered by, or under the supervision of, physicians to American Indians and Alaska Natives admitted as inpatients or outpatients.
    """

    zero7 = CodeSystemConcept(
        {
            "code": "07",
            "definition": "A facility or location owned and operated by a federally recognized American Indian or Alaska Native tribe or tribal organization under a 638 agreement, which provides diagnostic, therapeutic (surgical and nonsurgical), and rehabilitation services to tribal members who do not require hospitalization.",
            "display": "Tribal 638 Free-Standing Facility",
        }
    )
    """
    Tribal 638 Free-Standing Facility

    A facility or location owned and operated by a federally recognized American Indian or Alaska Native tribe or tribal organization under a 638 agreement, which provides diagnostic, therapeutic (surgical and nonsurgical), and rehabilitation services to tribal members who do not require hospitalization.
    """

    zero8 = CodeSystemConcept(
        {
            "code": "08",
            "definition": "A facility or location owned and operated by a federally recognized American Indian or Alaska Native tribe or tribal organization under a 638 agreement, which provides diagnostic, therapeutic (surgical and nonsurgical), and rehabilitation services to tribal members admitted as inpatients or outpatients.",
            "display": "Tribal 638 Provider-Based Facility",
        }
    )
    """
    Tribal 638 Provider-Based Facility

    A facility or location owned and operated by a federally recognized American Indian or Alaska Native tribe or tribal organization under a 638 agreement, which provides diagnostic, therapeutic (surgical and nonsurgical), and rehabilitation services to tribal members admitted as inpatients or outpatients.
    """

    zero9 = CodeSystemConcept(
        {
            "code": "09",
            "definition": "A prison, jail, reformatory, work farm, detention center, or any other similar facility maintained by either Federal, State or local authorities for the purpose of confinement or rehabilitation of adult or juvenile criminal offenders.",
            "display": "Prison/Correctional Facility",
        }
    )
    """
    Prison/Correctional Facility

    A prison, jail, reformatory, work farm, detention center, or any other similar facility maintained by either Federal, State or local authorities for the purpose of confinement or rehabilitation of adult or juvenile criminal offenders.
    """

    one1 = CodeSystemConcept(
        {
            "code": "11",
            "definition": "Location, other than a hospital, skilled nursing facility (SNF), military treatment facility, community health center, State or local public health clinic, or intermediate care facility (ICF), where the health professional routinely provides health examinations, diagnosis, and treatment of illness or injury on an ambulatory basis.",
            "display": "Office",
        }
    )
    """
    Office

    Location, other than a hospital, skilled nursing facility (SNF), military treatment facility, community health center, State or local public health clinic, or intermediate care facility (ICF), where the health professional routinely provides health examinations, diagnosis, and treatment of illness or injury on an ambulatory basis.
    """

    one2 = CodeSystemConcept(
        {
            "code": "12",
            "definition": "Location, other than a hospital or other facility, where the patient receives care in a private residence.",
            "display": "Home",
        }
    )
    """
    Home

    Location, other than a hospital or other facility, where the patient receives care in a private residence.
    """

    one3 = CodeSystemConcept(
        {
            "code": "13",
            "definition": "Congregate residential facility with self-contained living units providing assessment of each resident's needs and on-site support 24 hours a day, 7 days a week, with the capacity to deliver or arrange for services including some health care and other services.",
            "display": "Assisted Living Fa",
        }
    )
    """
    Assisted Living Fa

    Congregate residential facility with self-contained living units providing assessment of each resident's needs and on-site support 24 hours a day, 7 days a week, with the capacity to deliver or arrange for services including some health care and other services.
    """

    one4 = CodeSystemConcept(
        {
            "code": "14",
            "definition": "A residence, with shared living areas, where clients receive supervision and other services such as social and/or behavioral services, custodial service, and minimal services (e.g., medication administration).",
            "display": "Group Home",
        }
    )
    """
    Group Home

    A residence, with shared living areas, where clients receive supervision and other services such as social and/or behavioral services, custodial service, and minimal services (e.g., medication administration).
    """

    one5 = CodeSystemConcept(
        {
            "code": "15",
            "definition": "A facility/unit that moves from place-to-place equipped to provide preventive, screening, diagnostic, and/or treatment services.",
            "display": "Mobile Unit",
        }
    )
    """
    Mobile Unit

    A facility/unit that moves from place-to-place equipped to provide preventive, screening, diagnostic, and/or treatment services.
    """

    one9 = CodeSystemConcept(
        {
            "code": "19",
            "definition": "portion of an off-campus hospital provider-based department which provides diagnostic, therapeutic (both surgical and nonsurgical), and rehabilitation services to sick or injured persons who do not require hospitalization or institutionalization.",
            "display": "Off Campus-Outpatient Hospital",
        }
    )
    """
    Off Campus-Outpatient Hospital

    portion of an off-campus hospital provider-based department which provides diagnostic, therapeutic (both surgical and nonsurgical), and rehabilitation services to sick or injured persons who do not require hospitalization or institutionalization.
    """

    two0 = CodeSystemConcept(
        {
            "code": "20",
            "definition": "Location, distinct from a hospital emergency room, an office, or a clinic, whose purpose is to diagnose and treat illness or injury for unscheduled, ambulatory patients seeking immediate medical attention.",
            "display": "Urgent Care Facility",
        }
    )
    """
    Urgent Care Facility

    Location, distinct from a hospital emergency room, an office, or a clinic, whose purpose is to diagnose and treat illness or injury for unscheduled, ambulatory patients seeking immediate medical attention.
    """

    two1 = CodeSystemConcept(
        {
            "code": "21",
            "definition": "A facility, other than psychiatric, which primarily provides diagnostic, therapeutic (both surgical and nonsurgical), and rehabilitation services by, or under, the supervision of physicians to patients admitted for a variety of medical conditions.",
            "display": "Inpatient Hospital",
        }
    )
    """
    Inpatient Hospital

    A facility, other than psychiatric, which primarily provides diagnostic, therapeutic (both surgical and nonsurgical), and rehabilitation services by, or under, the supervision of physicians to patients admitted for a variety of medical conditions.
    """

    four1 = CodeSystemConcept(
        {
            "code": "41",
            "definition": "A land vehicle specifically designed, equipped and staffed for lifesaving and transporting the sick or injured.",
            "display": "Ambulance—Land",
        }
    )
    """
    Ambulance—Land

    A land vehicle specifically designed, equipped and staffed for lifesaving and transporting the sick or injured.
    """

    class Meta:
        resource = _resource
