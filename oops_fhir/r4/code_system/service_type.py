from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ServiceType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ServiceType:
    """
    Service type

    This value set defines an example set of codes of service-types.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/service-type
    """

    one = CodeSystemConcept(
        {
            "code": "1",
            "definition": "Adoption & permanent care information/support",
            "display": "Adoption/Permanent Care Info/Support",
        }
    )
    """
    Adoption/Permanent Care Info/Support

    Adoption & permanent care information/support
    """

    two = CodeSystemConcept(
        {
            "code": "2",
            "definition": "Aged care assessment",
            "display": "Aged Care Assessment",
        }
    )
    """
    Aged Care Assessment

    Aged care assessment
    """

    three = CodeSystemConcept(
        {
            "code": "3",
            "definition": "Aged Care information/referral",
            "display": "Aged Care Information/Referral",
        }
    )
    """
    Aged Care Information/Referral

    Aged Care information/referral
    """

    four = CodeSystemConcept(
        {
            "code": "4",
            "definition": "Aged Residential Care",
            "display": "Aged Residential Care",
        }
    )
    """
    Aged Residential Care

    Aged Residential Care
    """

    five = CodeSystemConcept(
        {
            "code": "5",
            "definition": "Case management for older persons",
            "display": "Case Management for Older Persons",
        }
    )
    """
    Case Management for Older Persons

    Case management for older persons
    """

    six = CodeSystemConcept(
        {
            "code": "6",
            "definition": "Delivered meals (meals on wheels)",
            "display": "Delivered Meals (Meals On Wheels)",
        }
    )
    """
    Delivered Meals (Meals On Wheels)

    Delivered meals (meals on wheels)
    """

    seven = CodeSystemConcept(
        {"code": "7", "definition": "Friendly visiting", "display": "Friendly Visiting"}
    )
    """
    Friendly Visiting

    Friendly visiting
    """

    eight = CodeSystemConcept(
        {
            "code": "8",
            "definition": "Home care/housekeeping assistance",
            "display": "Home Care/Housekeeping Assistance",
        }
    )
    """
    Home Care/Housekeeping Assistance

    Home care/housekeeping assistance
    """

    nine = CodeSystemConcept(
        {
            "code": "9",
            "definition": "Home maintenance and repair",
            "display": "Home Maintenance and Repair",
        }
    )
    """
    Home Maintenance and Repair

    Home maintenance and repair
    """

    one0 = CodeSystemConcept(
        {
            "code": "10",
            "definition": "Personal alarms/alerts",
            "display": "Personal Alarms/Alerts",
        }
    )
    """
    Personal Alarms/Alerts

    Personal alarms/alerts
    """

    one1 = CodeSystemConcept(
        {
            "code": "11",
            "definition": "Personal care for older persons",
            "display": "Personal Care for Older Persons",
        }
    )
    """
    Personal Care for Older Persons

    Personal care for older persons
    """

    one2 = CodeSystemConcept(
        {
            "code": "12",
            "definition": "Planned activity groups",
            "display": "Planned Activity Groups",
        }
    )
    """
    Planned Activity Groups

    Planned activity groups
    """

    one3 = CodeSystemConcept(
        {"code": "13", "definition": "Acupuncture", "display": "Acupuncture"}
    )
    """
    Acupuncture

    Acupuncture
    """

    one4 = CodeSystemConcept(
        {
            "code": "14",
            "definition": "Alexander technique therapy",
            "display": "Alexander Technique Therapy",
        }
    )
    """
    Alexander Technique Therapy

    Alexander technique therapy
    """

    one5 = CodeSystemConcept(
        {"code": "15", "definition": "Aromatherapy", "display": "Aromatherapy"}
    )
    """
    Aromatherapy

    Aromatherapy
    """

    one6 = CodeSystemConcept(
        {
            "code": "16",
            "definition": "Biorhythm services",
            "display": "Biorhythm Services",
        }
    )
    """
    Biorhythm Services

    Biorhythm services
    """

    one7 = CodeSystemConcept(
        {"code": "17", "definition": "Bowen therapy", "display": "Bowen Therapy"}
    )
    """
    Bowen Therapy

    Bowen therapy
    """

    one8 = CodeSystemConcept(
        {
            "code": "18",
            "definition": "Chinese herbal medicine",
            "display": "Chinese Herbal Medicine",
        }
    )
    """
    Chinese Herbal Medicine

    Chinese herbal medicine
    """

    one9 = CodeSystemConcept(
        {"code": "19", "definition": "Feldenkrais", "display": "Feldenkrais"}
    )
    """
    Feldenkrais

    Feldenkrais
    """

    two0 = CodeSystemConcept(
        {"code": "20", "definition": "Homoeopathy", "display": "Homoeopathy"}
    )
    """
    Homoeopathy

    Homoeopathy
    """

    two1 = CodeSystemConcept(
        {"code": "21", "definition": "Hydrotherapy", "display": "Hydrotherapy"}
    )
    """
    Hydrotherapy

    Hydrotherapy
    """

    two2 = CodeSystemConcept(
        {"code": "22", "definition": "Hypnotherapy", "display": "Hypnotherapy"}
    )
    """
    Hypnotherapy

    Hypnotherapy
    """

    two3 = CodeSystemConcept(
        {"code": "23", "definition": "Kinesiology", "display": "Kinesiology"}
    )
    """
    Kinesiology

    Kinesiology
    """

    two4 = CodeSystemConcept(
        {"code": "24", "definition": "Magnetic therapy", "display": "Magnetic Therapy"}
    )
    """
    Magnetic Therapy

    Magnetic therapy
    """

    two5 = CodeSystemConcept(
        {"code": "25", "definition": "Massage therapy", "display": "Massage Therapy"}
    )
    """
    Massage Therapy

    Massage therapy
    """

    two6 = CodeSystemConcept(
        {"code": "26", "definition": "Meditation", "display": "Meditation"}
    )
    """
    Meditation

    Meditation
    """

    two7 = CodeSystemConcept(
        {"code": "27", "definition": "Myotherapy", "display": "Myotherapy"}
    )
    """
    Myotherapy

    Myotherapy
    """

    two8 = CodeSystemConcept(
        {"code": "28", "definition": "Naturopathy", "display": "Naturopathy"}
    )
    """
    Naturopathy

    Naturopathy
    """

    two9 = CodeSystemConcept(
        {"code": "29", "definition": "Reflexology", "display": "Reflexology"}
    )
    """
    Reflexology

    Reflexology
    """

    three0 = CodeSystemConcept(
        {"code": "30", "definition": "Reiki", "display": "Reiki"}
    )
    """
    Reiki

    Reiki
    """

    three1 = CodeSystemConcept(
        {
            "code": "31",
            "definition": "Relaxation therapy",
            "display": "Relaxation Therapy",
        }
    )
    """
    Relaxation Therapy

    Relaxation therapy
    """

    three2 = CodeSystemConcept(
        {"code": "32", "definition": "Shiatsu", "display": "Shiatsu"}
    )
    """
    Shiatsu

    Shiatsu
    """

    three3 = CodeSystemConcept(
        {
            "code": "33",
            "definition": "Western herbal medicine",
            "display": "Western Herbal Medicine",
        }
    )
    """
    Western Herbal Medicine

    Western herbal medicine
    """

    three4 = CodeSystemConcept(
        {"code": "34", "definition": "Family day care", "display": "Family Day care"}
    )
    """
    Family Day care

    Family day care
    """

    three5 = CodeSystemConcept(
        {"code": "35", "definition": "Holiday programs", "display": "Holiday Programs"}
    )
    """
    Holiday Programs

    Holiday programs
    """

    three6 = CodeSystemConcept(
        {
            "code": "36",
            "definition": "Kindergarten inclusion support for children with a disability",
            "display": "Kindergarten Inclusion Support ",
        }
    )
    """
    Kindergarten Inclusion Support 

    Kindergarten inclusion support for children with a disability
    """

    three7 = CodeSystemConcept(
        {
            "code": "37",
            "definition": "Kindergarten/preschool",
            "display": "Kindergarten/Preschool",
        }
    )
    """
    Kindergarten/Preschool

    Kindergarten/preschool
    """

    three8 = CodeSystemConcept(
        {
            "code": "38",
            "definition": "Long day child care",
            "display": "Long Day Child Care",
        }
    )
    """
    Long Day Child Care

    Long day child care
    """

    three9 = CodeSystemConcept(
        {
            "code": "39",
            "definition": "Occasional child care",
            "display": "Occasional Child Care",
        }
    )
    """
    Occasional Child Care

    Occasional child care
    """

    four0 = CodeSystemConcept(
        {
            "code": "40",
            "definition": "Outside school hours care",
            "display": "Outside School Hours Care",
        }
    )
    """
    Outside School Hours Care

    Outside school hours care
    """

    four1 = CodeSystemConcept(
        {
            "code": "41",
            "definition": "Children's play programs",
            "display": "Children's Play Programs",
        }
    )
    """
    Children's Play Programs

    Children's play programs
    """

    four2 = CodeSystemConcept(
        {
            "code": "42",
            "definition": "Parenting & family management support/education",
            "display": "Parenting/Family Support/Education",
        }
    )
    """
    Parenting/Family Support/Education

    Parenting & family management support/education
    """

    four3 = CodeSystemConcept(
        {"code": "43", "definition": "Playgroup", "display": "Playgroup"}
    )
    """
    Playgroup

    Playgroup
    """

    four4 = CodeSystemConcept(
        {"code": "44", "definition": "School nursing", "display": "School Nursing"}
    )
    """
    School Nursing

    School nursing
    """

    four5 = CodeSystemConcept(
        {"code": "45", "definition": "Toy library", "display": "Toy Library"}
    )
    """
    Toy Library

    Toy library
    """

    four6 = CodeSystemConcept(
        {
            "code": "46",
            "definition": "Child protection/child abuse report",
            "display": "Child Protection/Child Abuse Report",
        }
    )
    """
    Child Protection/Child Abuse Report

    Child protection/child abuse report
    """

    four7 = CodeSystemConcept(
        {"code": "47", "definition": "Foster care", "display": "Foster Care"}
    )
    """
    Foster Care

    Foster care
    """

    four8 = CodeSystemConcept(
        {
            "code": "48",
            "definition": "Residential/ out of home care",
            "display": "Residential/Out-of-Home Care",
        }
    )
    """
    Residential/Out-of-Home Care

    Residential/ out of home care
    """

    four9 = CodeSystemConcept(
        {
            "code": "49",
            "definition": "Support for young people leaving care",
            "display": "Support - Young People Leaving Care",
        }
    )
    """
    Support - Young People Leaving Care

    Support for young people leaving care
    """

    five0 = CodeSystemConcept(
        {"code": "50", "definition": "Audiology", "display": "Audiology"}
    )
    """
    Audiology

    Audiology
    """

    five1 = CodeSystemConcept(
        {"code": "51", "definition": "Blood donation", "display": "Blood Donation"}
    )
    """
    Blood Donation

    Blood donation
    """

    five2 = CodeSystemConcept(
        {"code": "52", "definition": "Chiropractic", "display": "Chiropractic"}
    )
    """
    Chiropractic

    Chiropractic
    """

    five3 = CodeSystemConcept(
        {"code": "53", "definition": "Dietetics", "display": "Dietetics"}
    )
    """
    Dietetics

    Dietetics
    """

    five4 = CodeSystemConcept(
        {"code": "54", "definition": "Family planning", "display": "Family Planning"}
    )
    """
    Family Planning

    Family planning
    """

    five5 = CodeSystemConcept(
        {
            "code": "55",
            "definition": "Health advocacy/Liaison service",
            "display": "Health Advocacy/Liaison Service",
        }
    )
    """
    Health Advocacy/Liaison Service

    Health advocacy/Liaison service
    """

    five6 = CodeSystemConcept(
        {
            "code": "56",
            "definition": "Health information/referral",
            "display": "Health Information/Referral",
        }
    )
    """
    Health Information/Referral

    Health information/referral
    """

    five7 = CodeSystemConcept(
        {"code": "57", "definition": "Immunization", "display": "Immunization"}
    )
    """
    Immunization

    Immunization
    """

    five8 = CodeSystemConcept(
        {
            "code": "58",
            "definition": "Maternal & child health",
            "display": "Maternal & Child Health",
        }
    )
    """
    Maternal & Child Health

    Maternal & child health
    """

    five9 = CodeSystemConcept(
        {"code": "59", "definition": "Nursing", "display": "Nursing"}
    )
    """
    Nursing

    Nursing
    """

    six0 = CodeSystemConcept(
        {"code": "60", "definition": "Nutrition", "display": "Nutrition"}
    )
    """
    Nutrition

    Nutrition
    """

    six1 = CodeSystemConcept(
        {
            "code": "61",
            "definition": "Occupational therapy",
            "display": "Occupational Therapy",
        }
    )
    """
    Occupational Therapy

    Occupational therapy
    """

    six2 = CodeSystemConcept(
        {"code": "62", "definition": "Optometry", "display": "Optometry"}
    )
    """
    Optometry

    Optometry
    """

    six3 = CodeSystemConcept(
        {"code": "63", "definition": "Osteopathy", "display": "Osteopathy"}
    )
    """
    Osteopathy

    Osteopathy
    """

    six4 = CodeSystemConcept(
        {"code": "64", "definition": "Pharmacy", "display": "Pharmacy"}
    )
    """
    Pharmacy

    Pharmacy
    """

    six5 = CodeSystemConcept(
        {"code": "65", "definition": "Physiotherapy", "display": "Physiotherapy"}
    )
    """
    Physiotherapy

    Physiotherapy
    """

    six6 = CodeSystemConcept(
        {"code": "66", "definition": "Podiatry", "display": "Podiatry"}
    )
    """
    Podiatry

    Podiatry
    """

    six7 = CodeSystemConcept(
        {"code": "67", "definition": "Sexual health", "display": "Sexual Health"}
    )
    """
    Sexual Health

    Sexual health
    """

    six8 = CodeSystemConcept(
        {
            "code": "68",
            "definition": "Speech pathology/therapy",
            "display": "Speech Pathology/Therapy",
        }
    )
    """
    Speech Pathology/Therapy

    Speech pathology/therapy
    """

    six9 = CodeSystemConcept(
        {
            "code": "69",
            "definition": "Bereavement counselling",
            "display": "Bereavement Counselling",
        }
    )
    """
    Bereavement Counselling

    Bereavement counselling
    """

    seven0 = CodeSystemConcept(
        {
            "code": "70",
            "definition": "Crisis counselling",
            "display": "Crisis Counselling",
        }
    )
    """
    Crisis Counselling

    Crisis counselling
    """

    seven1 = CodeSystemConcept(
        {
            "code": "71",
            "definition": "Family counselling and/or family therapy",
            "display": "Family Counselling/Therapy",
        }
    )
    """
    Family Counselling/Therapy

    Family counselling and/or family therapy
    """

    seven2 = CodeSystemConcept(
        {
            "code": "72",
            "definition": "Family violence counselling",
            "display": "Family Violence Counselling",
        }
    )
    """
    Family Violence Counselling

    Family violence counselling
    """

    seven3 = CodeSystemConcept(
        {
            "code": "73",
            "definition": "Financial counselling",
            "display": "Financial Counselling",
        }
    )
    """
    Financial Counselling

    Financial counselling
    """

    seven4 = CodeSystemConcept(
        {
            "code": "74",
            "definition": "Generalist counselling",
            "display": "Generalist Counselling",
        }
    )
    """
    Generalist Counselling

    Generalist counselling
    """

    seven5 = CodeSystemConcept(
        {
            "code": "75",
            "definition": "Genetic counselling",
            "display": "Genetic Counselling",
        }
    )
    """
    Genetic Counselling

    Genetic counselling
    """

    seven6 = CodeSystemConcept(
        {
            "code": "76",
            "definition": "Health counselling",
            "display": "Health Counselling",
        }
    )
    """
    Health Counselling

    Health counselling
    """

    seven7 = CodeSystemConcept(
        {"code": "77", "definition": "Mediation", "display": "Mediation"}
    )
    """
    Mediation

    Mediation
    """

    seven8 = CodeSystemConcept(
        {
            "code": "78",
            "definition": "Problem gambling counselling",
            "display": "Problem Gambling Counselling",
        }
    )
    """
    Problem Gambling Counselling

    Problem gambling counselling
    """

    seven9 = CodeSystemConcept(
        {
            "code": "79",
            "definition": "Relationship counselling",
            "display": "Relationship Counselling",
        }
    )
    """
    Relationship Counselling

    Relationship counselling
    """

    eight0 = CodeSystemConcept(
        {
            "code": "80",
            "definition": "Sexual assault counselling",
            "display": "Sexual Assault Counselling",
        }
    )
    """
    Sexual Assault Counselling

    Sexual assault counselling
    """

    eight1 = CodeSystemConcept(
        {
            "code": "81",
            "definition": "Trauma counselling",
            "display": "Trauma Counselling",
        }
    )
    """
    Trauma Counselling

    Trauma counselling
    """

    eight2 = CodeSystemConcept(
        {
            "code": "82",
            "definition": "Victims of crime counselling",
            "display": "Victims of Crime Counselling",
        }
    )
    """
    Victims of Crime Counselling

    Victims of crime counselling
    """

    eight3 = CodeSystemConcept(
        {
            "code": "83",
            "definition": "Cemetery operation",
            "display": "Cemetery Operation",
        }
    )
    """
    Cemetery Operation

    Cemetery operation
    """

    eight4 = CodeSystemConcept(
        {"code": "84", "definition": "Cremation", "display": "Cremation"}
    )
    """
    Cremation

    Cremation
    """

    eight5 = CodeSystemConcept(
        {
            "code": "85",
            "definition": "Death service information",
            "display": "Death Service Information",
        }
    )
    """
    Death Service Information

    Death service information
    """

    eight6 = CodeSystemConcept(
        {"code": "86", "definition": "Funeral services", "display": "Funeral Services"}
    )
    """
    Funeral Services

    Funeral services
    """

    eight7 = CodeSystemConcept(
        {"code": "87", "definition": "Endodontic", "display": "Endodontic"}
    )
    """
    Endodontic

    Endodontic
    """

    eight8 = CodeSystemConcept(
        {"code": "88", "definition": "General dental", "display": "General Dental"}
    )
    """
    General Dental

    General dental
    """

    eight9 = CodeSystemConcept(
        {"code": "89", "definition": "Oral medicine", "display": "Oral Medicine"}
    )
    """
    Oral Medicine

    Oral medicine
    """

    nine0 = CodeSystemConcept(
        {"code": "90", "definition": "Oral surgery", "display": "Oral Surgery"}
    )
    """
    Oral Surgery

    Oral surgery
    """

    nine1 = CodeSystemConcept(
        {"code": "91", "definition": "Orthodontic", "display": "Orthodontic"}
    )
    """
    Orthodontic

    Orthodontic
    """

    nine2 = CodeSystemConcept(
        {
            "code": "92",
            "definition": "Paediatric Dentistry",
            "display": "Paediatric Dentistry",
        }
    )
    """
    Paediatric Dentistry

    Paediatric Dentistry
    """

    nine3 = CodeSystemConcept(
        {"code": "93", "definition": "Periodontic", "display": "Periodontic"}
    )
    """
    Periodontic

    Periodontic
    """

    nine4 = CodeSystemConcept(
        {"code": "94", "definition": "Prosthodontic", "display": "Prosthodontic"}
    )
    """
    Prosthodontic

    Prosthodontic
    """

    nine5 = CodeSystemConcept(
        {
            "code": "95",
            "definition": "Acquired brain injury information/referral",
            "display": "Acquired Brain Injury Info/Referral",
        }
    )
    """
    Acquired Brain Injury Info/Referral

    Acquired brain injury information/referral
    """

    nine6 = CodeSystemConcept(
        {
            "code": "96",
            "definition": "Disability advocacy",
            "display": "Disability Advocacy",
        }
    )
    """
    Disability Advocacy

    Disability advocacy
    """

    nine7 = CodeSystemConcept(
        {
            "code": "97",
            "definition": "Disability aids & equipment",
            "display": "Disability Aids & Equipment",
        }
    )
    """
    Disability Aids & Equipment

    Disability aids & equipment
    """

    nine8 = CodeSystemConcept(
        {
            "code": "98",
            "definition": "Disability case management",
            "display": "Disability Case Management",
        }
    )
    """
    Disability Case Management

    Disability case management
    """

    nine9 = CodeSystemConcept(
        {
            "code": "99",
            "definition": "Disability day programs & activities",
            "display": "Disability Day Programs/Activities",
        }
    )
    """
    Disability Day Programs/Activities

    Disability day programs & activities
    """

    one00 = CodeSystemConcept(
        {
            "code": "100",
            "definition": "Disability information/referral",
            "display": "Disability Information/Referral",
        }
    )
    """
    Disability Information/Referral

    Disability information/referral
    """

    one01 = CodeSystemConcept(
        {
            "code": "101",
            "definition": "Disability support packages",
            "display": "Disability Support Packages",
        }
    )
    """
    Disability Support Packages

    Disability support packages
    """

    one02 = CodeSystemConcept(
        {
            "code": "102",
            "definition": "Disability supported accommodation",
            "display": "Disability Supported Accommodation",
        }
    )
    """
    Disability Supported Accommodation

    Disability supported accommodation
    """

    one03 = CodeSystemConcept(
        {
            "code": "103",
            "definition": "Early childhood intervention",
            "display": "Early Childhood Intervention",
        }
    )
    """
    Early Childhood Intervention

    Early childhood intervention
    """

    one04 = CodeSystemConcept(
        {
            "code": "104",
            "definition": "Hearing aids & equipment",
            "display": "Hearing Aids & Equipment",
        }
    )
    """
    Hearing Aids & Equipment

    Hearing aids & equipment
    """

    one05 = CodeSystemConcept(
        {
            "code": "105",
            "definition": "Drug and/or alcohol counselling",
            "display": "Drug and/or Alcohol Counselling",
        }
    )
    """
    Drug and/or Alcohol Counselling

    Drug and/or alcohol counselling
    """

    one06 = CodeSystemConcept(
        {
            "code": "106",
            "definition": "Drug and/or alcohol information/referral",
            "display": "Drug/Alcohol Information/Referral",
        }
    )
    """
    Drug/Alcohol Information/Referral

    Drug and/or alcohol information/referral
    """

    one07 = CodeSystemConcept(
        {
            "code": "107",
            "definition": "Needle & Syringe exchange",
            "display": "Needle & Syringe Exchange",
        }
    )
    """
    Needle & Syringe Exchange

    Needle & Syringe exchange
    """

    one08 = CodeSystemConcept(
        {
            "code": "108",
            "definition": "Non-residential alcohol and/or drug dependence treatment",
            "display": "Non-resid. Alcohol/Drug Treatment ",
        }
    )
    """
    Non-resid. Alcohol/Drug Treatment 

    Non-residential alcohol and/or drug dependence treatment
    """

    one09 = CodeSystemConcept(
        {
            "code": "109",
            "definition": "Pharmacotherapy (eg. methadone) program",
            "display": "Pharmacotherapy",
        }
    )
    """
    Pharmacotherapy

    Pharmacotherapy (eg. methadone) program
    """

    one10 = CodeSystemConcept(
        {"code": "110", "definition": "Quit program", "display": "Quit Program"}
    )
    """
    Quit Program

    Quit program
    """

    one11 = CodeSystemConcept(
        {
            "code": "111",
            "definition": "Residential alcohol and/or drug dependence treatment",
            "display": "Residential Alcohol/Drug Treatment ",
        }
    )
    """
    Residential Alcohol/Drug Treatment 

    Residential alcohol and/or drug dependence treatment
    """

    one12 = CodeSystemConcept(
        {
            "code": "112",
            "definition": "Adult/community education",
            "display": "Adult/Community Education",
        }
    )
    """
    Adult/Community Education

    Adult/community education
    """

    one13 = CodeSystemConcept(
        {"code": "113", "definition": "Higher education", "display": "Higher Education"}
    )
    """
    Higher Education

    Higher education
    """

    one14 = CodeSystemConcept(
        {
            "code": "114",
            "definition": "Primary education",
            "display": "Primary Education",
        }
    )
    """
    Primary Education

    Primary education
    """

    one15 = CodeSystemConcept(
        {
            "code": "115",
            "definition": "Secondary education",
            "display": "Secondary Education",
        }
    )
    """
    Secondary Education

    Secondary education
    """

    one16 = CodeSystemConcept(
        {
            "code": "116",
            "definition": "Training & vocational education",
            "display": "Training & Vocational Education",
        }
    )
    """
    Training & Vocational Education

    Training & vocational education
    """

    one17 = CodeSystemConcept(
        {
            "code": "117",
            "definition": "Emergency medical",
            "display": "Emergency Medical",
        }
    )
    """
    Emergency Medical

    Emergency medical
    """

    one18 = CodeSystemConcept(
        {
            "code": "118",
            "definition": "Employment placement and/or support",
            "display": "Employment Placement and/or Support",
        }
    )
    """
    Employment Placement and/or Support

    Employment placement and/or support
    """

    one19 = CodeSystemConcept(
        {
            "code": "119",
            "definition": "Vocational Rehabilitation",
            "display": "Vocational Rehabilitation",
        }
    )
    """
    Vocational Rehabilitation

    Vocational Rehabilitation
    """

    one20 = CodeSystemConcept(
        {
            "code": "120",
            "definition": "Workplace safety and/or accident prevention",
            "display": "Work Safety/Accident Prevention",
        }
    )
    """
    Work Safety/Accident Prevention

    Workplace safety and/or accident prevention
    """

    one21 = CodeSystemConcept(
        {
            "code": "121",
            "definition": "Financial assistance",
            "display": "Financial Assistance",
        }
    )
    """
    Financial Assistance

    Financial assistance
    """

    one22 = CodeSystemConcept(
        {
            "code": "122",
            "definition": "Financial information/advice",
            "display": "Financial Information/Advice",
        }
    )
    """
    Financial Information/Advice

    Financial information/advice
    """

    one23 = CodeSystemConcept(
        {"code": "123", "definition": "Material aid", "display": "Material Aid"}
    )
    """
    Material Aid

    Material aid
    """

    one24 = CodeSystemConcept(
        {
            "code": "124",
            "definition": "General Practice/GP (doctor)",
            "display": "General Practice",
        }
    )
    """
    General Practice

    General Practice/GP (doctor)
    """

    one25 = CodeSystemConcept(
        {
            "code": "125",
            "definition": "Accommodation placement and/or support",
            "display": "Accommodation Placement/Support",
        }
    )
    """
    Accommodation Placement/Support

    Accommodation placement and/or support
    """

    one26 = CodeSystemConcept(
        {
            "code": "126",
            "definition": "Crisis/emergency accommodation",
            "display": "Crisis/Emergency Accommodation",
        }
    )
    """
    Crisis/Emergency Accommodation

    Crisis/emergency accommodation
    """

    one27 = CodeSystemConcept(
        {
            "code": "127",
            "definition": "Homelessness support",
            "display": "Homelessness Support",
        }
    )
    """
    Homelessness Support

    Homelessness support
    """

    one28 = CodeSystemConcept(
        {
            "code": "128",
            "definition": "Housing information/referral",
            "display": "Housing Information/Referral",
        }
    )
    """
    Housing Information/Referral

    Housing information/referral
    """

    one29 = CodeSystemConcept(
        {
            "code": "129",
            "definition": "Public rental housing",
            "display": "Public Rental Housing",
        }
    )
    """
    Public Rental Housing

    Public rental housing
    """

    one30 = CodeSystemConcept(
        {
            "code": "130",
            "definition": "Interpreting/Multilingual/Language service",
            "display": "Interpreting/Multilingual Service",
        }
    )
    """
    Interpreting/Multilingual Service

    Interpreting/Multilingual/Language service
    """

    one31 = CodeSystemConcept(
        {"code": "131", "definition": "Juvenile Justice", "display": "Juvenile Justice"}
    )
    """
    Juvenile Justice

    Juvenile Justice
    """

    one32 = CodeSystemConcept(
        {"code": "132", "definition": "Legal advocacy", "display": "Legal Advocacy"}
    )
    """
    Legal Advocacy

    Legal advocacy
    """

    one33 = CodeSystemConcept(
        {
            "code": "133",
            "definition": "Legal information/advice/referral",
            "display": "Legal Information/Advice/Referral",
        }
    )
    """
    Legal Information/Advice/Referral

    Legal information/advice/referral
    """

    one34 = CodeSystemConcept(
        {
            "code": "134",
            "definition": "Mental health advocacy",
            "display": "Mental Health Advocacy",
        }
    )
    """
    Mental Health Advocacy

    Mental health advocacy
    """

    one35 = CodeSystemConcept(
        {
            "code": "135",
            "definition": "Mental health assessment/triage/crisis response",
            "display": "Mental Health Assess/Triage/Crisis Response",
        }
    )
    """
    Mental Health Assess/Triage/Crisis Response

    Mental health assessment/triage/crisis response
    """

    one36 = CodeSystemConcept(
        {
            "code": "136",
            "definition": "Mental health case management/continuing care",
            "display": "Mental Health Case Management",
        }
    )
    """
    Mental Health Case Management

    Mental health case management/continuing care
    """

    one37 = CodeSystemConcept(
        {
            "code": "137",
            "definition": "Mental health information/referral",
            "display": "Mental Health Information/Referral",
        }
    )
    """
    Mental Health Information/Referral

    Mental health information/referral
    """

    one38 = CodeSystemConcept(
        {
            "code": "138",
            "definition": "Mental health inpatient services (hospital psychiatric unit) - requires referral",
            "display": "Mental Health Inpatient Services",
        }
    )
    """
    Mental Health Inpatient Services

    Mental health inpatient services (hospital psychiatric unit) - requires referral
    """

    one39 = CodeSystemConcept(
        {
            "code": "139",
            "definition": "Mental health non-residential rehabilitation",
            "display": "Mental Health Non-residential Rehab",
        }
    )
    """
    Mental Health Non-residential Rehab

    Mental health non-residential rehabilitation
    """

    one40 = CodeSystemConcept(
        {
            "code": "140",
            "definition": "Mental health residential rehabilitation/community care unit",
            "display": "Mental Health Residential Rehab/CCU",
        }
    )
    """
    Mental Health Residential Rehab/CCU

    Mental health residential rehabilitation/community care unit
    """

    one41 = CodeSystemConcept(
        {
            "code": "141",
            "definition": "Psychiatry (requires referral)",
            "display": "Psychiatry (Requires Referral)",
        }
    )
    """
    Psychiatry (Requires Referral)

    Psychiatry (requires referral)
    """

    one42 = CodeSystemConcept(
        {"code": "142", "definition": "Psychology", "display": "Psychology"}
    )
    """
    Psychology

    Psychology
    """

    one43 = CodeSystemConcept(
        {"code": "143", "definition": "Martial arts", "display": "Martial Arts"}
    )
    """
    Martial Arts

    Martial arts
    """

    one44 = CodeSystemConcept(
        {
            "code": "144",
            "definition": "Personal fitness training",
            "display": "Personal Fitness Training",
        }
    )
    """
    Personal Fitness Training

    Personal fitness training
    """

    one45 = CodeSystemConcept(
        {
            "code": "145",
            "definition": "Physical activity group",
            "display": "Physical Activity Group",
        }
    )
    """
    Physical Activity Group

    Physical activity group
    """

    one46 = CodeSystemConcept(
        {
            "code": "146",
            "definition": "Physical activity programs",
            "display": "Physical Activity Programs",
        }
    )
    """
    Physical Activity Programs

    Physical activity programs
    """

    one47 = CodeSystemConcept(
        {
            "code": "147",
            "definition": "Physical fitness testing",
            "display": "Physical Fitness Testing",
        }
    )
    """
    Physical Fitness Testing

    Physical fitness testing
    """

    one48 = CodeSystemConcept(
        {"code": "148", "definition": "Pilates", "display": "Pilates"}
    )
    """
    Pilates

    Pilates
    """

    one49 = CodeSystemConcept(
        {"code": "149", "definition": "Self defence", "display": "Self-Defence"}
    )
    """
    Self-Defence

    Self defence
    """

    one50 = CodeSystemConcept(
        {"code": "150", "definition": "Sporting club", "display": "Sporting Club"}
    )
    """
    Sporting Club

    Sporting club
    """

    one51 = CodeSystemConcept({"code": "151", "definition": "Yoga", "display": "Yoga"})
    """
    Yoga

    Yoga
    """

    one52 = CodeSystemConcept(
        {"code": "152", "definition": "Food safety", "display": "Food Safety"}
    )
    """
    Food Safety

    Food safety
    """

    one53 = CodeSystemConcept(
        {
            "code": "153",
            "definition": "Health regulatory, inspection and/or certification",
            "display": "Health Regulatory /Inspection /Cert.",
        }
    )
    """
    Health Regulatory /Inspection /Cert.

    Health regulatory, inspection and/or certification
    """

    one54 = CodeSystemConcept(
        {
            "code": "154",
            "definition": "Workplace health and/or safety inspection and/or certification",
            "display": "Work Health/Safety Inspection/Cert.",
        }
    )
    """
    Work Health/Safety Inspection/Cert.

    Workplace health and/or safety inspection and/or certification
    """

    one55 = CodeSystemConcept(
        {"code": "155", "definition": "Carer support", "display": "Carer Support"}
    )
    """
    Carer Support

    Carer support
    """

    one56 = CodeSystemConcept(
        {"code": "156", "definition": "Respite care", "display": "Respite Care"}
    )
    """
    Respite Care

    Respite care
    """

    one57 = CodeSystemConcept(
        {
            "code": "157",
            "definition": "Anatomical Pathology (including Cytopathology & Forensic Pathology)",
            "display": "Anatomical Pathology ",
        }
    )
    """
    Anatomical Pathology 

    Anatomical Pathology (including Cytopathology & Forensic Pathology)
    """

    one58 = CodeSystemConcept(
        {
            "code": "158",
            "definition": "Pathology - Clinical Chemistry",
            "display": "Pathology - Clinical Chemistry",
        }
    )
    """
    Pathology - Clinical Chemistry

    Pathology - Clinical Chemistry
    """

    one59 = CodeSystemConcept(
        {
            "code": "159",
            "definition": "Pathology - General",
            "display": "Pathology - General",
        }
    )
    """
    Pathology - General

    Pathology - General
    """

    one60 = CodeSystemConcept(
        {
            "code": "160",
            "definition": "Pathology - Genetics",
            "display": "Pathology - Genetics",
        }
    )
    """
    Pathology - Genetics

    Pathology - Genetics
    """

    one61 = CodeSystemConcept(
        {
            "code": "161",
            "definition": "Pathology - Haematology",
            "display": "Pathology - Haematology",
        }
    )
    """
    Pathology - Haematology

    Pathology - Haematology
    """

    one62 = CodeSystemConcept(
        {
            "code": "162",
            "definition": "Pathology - Immunology",
            "display": "Pathology - Immunology",
        }
    )
    """
    Pathology - Immunology

    Pathology - Immunology
    """

    one63 = CodeSystemConcept(
        {
            "code": "163",
            "definition": "Pathology - Microbiology",
            "display": "Pathology - Microbiology",
        }
    )
    """
    Pathology - Microbiology

    Pathology - Microbiology
    """

    one64 = CodeSystemConcept(
        {
            "code": "164",
            "definition": "Anaesthesiology - Pain Medicine",
            "display": "Anaesthesiology - Pain Medicine",
        }
    )
    """
    Anaesthesiology - Pain Medicine

    Anaesthesiology - Pain Medicine
    """

    one65 = CodeSystemConcept(
        {"code": "165", "definition": "Cardiology", "display": "Cardiology"}
    )
    """
    Cardiology

    Cardiology
    """

    one66 = CodeSystemConcept(
        {
            "code": "166",
            "definition": "Clinical Genetics",
            "display": "Clinical Genetics",
        }
    )
    """
    Clinical Genetics

    Clinical Genetics
    """

    one67 = CodeSystemConcept(
        {
            "code": "167",
            "definition": "Clinical Pharmacology",
            "display": "Clinical Pharmacology",
        }
    )
    """
    Clinical Pharmacology

    Clinical Pharmacology
    """

    one68 = CodeSystemConcept(
        {"code": "168", "definition": "Dermatology", "display": "Dermatology"}
    )
    """
    Dermatology

    Dermatology
    """

    one69 = CodeSystemConcept(
        {"code": "169", "definition": "Endocrinology", "display": "Endocrinology"}
    )
    """
    Endocrinology

    Endocrinology
    """

    one70 = CodeSystemConcept(
        {
            "code": "170",
            "definition": "Gastroenterology & Hepatology",
            "display": "Gastroenterology & Hepatology",
        }
    )
    """
    Gastroenterology & Hepatology

    Gastroenterology & Hepatology
    """

    one71 = CodeSystemConcept(
        {
            "code": "171",
            "definition": "Geriatric medicine",
            "display": "Geriatric Medicine",
        }
    )
    """
    Geriatric Medicine

    Geriatric medicine
    """

    one72 = CodeSystemConcept(
        {
            "code": "172",
            "definition": "Immunology & Allergy",
            "display": "Immunology & Allergy",
        }
    )
    """
    Immunology & Allergy

    Immunology & Allergy
    """

    one73 = CodeSystemConcept(
        {
            "code": "173",
            "definition": "Infectious diseases",
            "display": "Infectious Diseases",
        }
    )
    """
    Infectious Diseases

    Infectious diseases
    """

    one74 = CodeSystemConcept(
        {
            "code": "174",
            "definition": "Intensive care medicine",
            "display": "Intensive Care Medicine",
        }
    )
    """
    Intensive Care Medicine

    Intensive care medicine
    """

    one75 = CodeSystemConcept(
        {"code": "175", "definition": "Medical Oncology", "display": "Medical Oncology"}
    )
    """
    Medical Oncology

    Medical Oncology
    """

    one76 = CodeSystemConcept(
        {"code": "176", "definition": "Nephrology", "display": "Nephrology"}
    )
    """
    Nephrology

    Nephrology
    """

    one77 = CodeSystemConcept(
        {"code": "177", "definition": "Neurology", "display": "Neurology"}
    )
    """
    Neurology

    Neurology
    """

    one78 = CodeSystemConcept(
        {
            "code": "178",
            "definition": "Occupational Medicine",
            "display": "Occupational Medicine",
        }
    )
    """
    Occupational Medicine

    Occupational Medicine
    """

    one79 = CodeSystemConcept(
        {
            "code": "179",
            "definition": "Palliative Medicine",
            "display": "Palliative Medicine",
        }
    )
    """
    Palliative Medicine

    Palliative Medicine
    """

    one80 = CodeSystemConcept(
        {
            "code": "180",
            "definition": "Public Health Medicine",
            "display": "Public Health Medicine",
        }
    )
    """
    Public Health Medicine

    Public Health Medicine
    """

    one81 = CodeSystemConcept(
        {
            "code": "181",
            "definition": "Rehabilitation Medicine",
            "display": "Rehabilitation Medicine",
        }
    )
    """
    Rehabilitation Medicine

    Rehabilitation Medicine
    """

    one82 = CodeSystemConcept(
        {"code": "182", "definition": "Rheumatology", "display": "Rheumatology"}
    )
    """
    Rheumatology

    Rheumatology
    """

    one83 = CodeSystemConcept(
        {"code": "183", "definition": "Sleep Medicine", "display": "Sleep Medicine"}
    )
    """
    Sleep Medicine

    Sleep Medicine
    """

    one84 = CodeSystemConcept(
        {
            "code": "184",
            "definition": "Thoracic medicine",
            "display": "Thoracic Medicine",
        }
    )
    """
    Thoracic Medicine

    Thoracic medicine
    """

    one85 = CodeSystemConcept(
        {
            "code": "185",
            "definition": "Gynaecological Oncology",
            "display": "Gynaecological Oncology",
        }
    )
    """
    Gynaecological Oncology

    Gynaecological Oncology
    """

    one86 = CodeSystemConcept(
        {
            "code": "186",
            "definition": "Obstetrics & Gynaecology",
            "display": "Obstetrics & Gynaecology",
        }
    )
    """
    Obstetrics & Gynaecology

    Obstetrics & Gynaecology
    """

    one87 = CodeSystemConcept(
        {
            "code": "187",
            "definition": "Reproductive Endocrinology & Infertility",
            "display": "Reproductive Endocrinology/Infertility",
        }
    )
    """
    Reproductive Endocrinology/Infertility

    Reproductive Endocrinology & Infertility
    """

    one88 = CodeSystemConcept(
        {"code": "188", "definition": "Urogynaecology", "display": "Urogynaecology"}
    )
    """
    Urogynaecology

    Urogynaecology
    """

    one89 = CodeSystemConcept(
        {
            "code": "189",
            "definition": "Neonatology & Perinatology",
            "display": "Neonatology & Perinatology",
        }
    )
    """
    Neonatology & Perinatology

    Neonatology & Perinatology
    """

    one90 = CodeSystemConcept(
        {
            "code": "190",
            "definition": "Paediatric Cardiology",
            "display": "Paediatric Cardiology",
        }
    )
    """
    Paediatric Cardiology

    Paediatric Cardiology
    """

    one91 = CodeSystemConcept(
        {
            "code": "191",
            "definition": "Paediatric Clinical Genetics",
            "display": "Paediatric Clinical Genetics",
        }
    )
    """
    Paediatric Clinical Genetics

    Paediatric Clinical Genetics
    """

    one92 = CodeSystemConcept(
        {
            "code": "192",
            "definition": "Paediatric Clinical Pharmacology",
            "display": "Paediatric Clinical Pharmacology",
        }
    )
    """
    Paediatric Clinical Pharmacology

    Paediatric Clinical Pharmacology
    """

    one93 = CodeSystemConcept(
        {
            "code": "193",
            "definition": "Paediatric Endocrinology",
            "display": "Paediatric Endocrinology",
        }
    )
    """
    Paediatric Endocrinology

    Paediatric Endocrinology
    """

    one94 = CodeSystemConcept(
        {
            "code": "194",
            "definition": "Paediatric Gastroenterology & Hepatology",
            "display": "Paed. Gastroenterology/Hepatology",
        }
    )
    """
    Paed. Gastroenterology/Hepatology

    Paediatric Gastroenterology & Hepatology
    """

    one95 = CodeSystemConcept(
        {
            "code": "195",
            "definition": "Paediatric Haematology",
            "display": "Paediatric Haematology",
        }
    )
    """
    Paediatric Haematology

    Paediatric Haematology
    """

    one96 = CodeSystemConcept(
        {
            "code": "196",
            "definition": "Paediatric Immunology & Allergy",
            "display": "Paediatric Immunology & Allergy",
        }
    )
    """
    Paediatric Immunology & Allergy

    Paediatric Immunology & Allergy
    """

    one97 = CodeSystemConcept(
        {
            "code": "197",
            "definition": "Paediatric Infectious diseases",
            "display": "Paediatric Infectious Diseases",
        }
    )
    """
    Paediatric Infectious Diseases

    Paediatric Infectious diseases
    """

    one98 = CodeSystemConcept(
        {
            "code": "198",
            "definition": "Paediatric intensive care medicine",
            "display": "Paediatric Intensive Care Medicine",
        }
    )
    """
    Paediatric Intensive Care Medicine

    Paediatric intensive care medicine
    """

    one99 = CodeSystemConcept(
        {
            "code": "199",
            "definition": "Paediatric Medical Oncology",
            "display": "Paediatric Medical Oncology",
        }
    )
    """
    Paediatric Medical Oncology

    Paediatric Medical Oncology
    """

    two00 = CodeSystemConcept(
        {
            "code": "200",
            "definition": "Paediatric Medicine",
            "display": "Paediatric Medicine",
        }
    )
    """
    Paediatric Medicine

    Paediatric Medicine
    """

    two01 = CodeSystemConcept(
        {
            "code": "201",
            "definition": "Paediatric Nephrology",
            "display": "Paediatric Nephrology",
        }
    )
    """
    Paediatric Nephrology

    Paediatric Nephrology
    """

    two02 = CodeSystemConcept(
        {
            "code": "202",
            "definition": "Paediatric Neurology",
            "display": "Paediatric Neurology",
        }
    )
    """
    Paediatric Neurology

    Paediatric Neurology
    """

    two03 = CodeSystemConcept(
        {
            "code": "203",
            "definition": "Paediatric Nuclear Medicine",
            "display": "Paediatric Nuclear Medicine",
        }
    )
    """
    Paediatric Nuclear Medicine

    Paediatric Nuclear Medicine
    """

    two04 = CodeSystemConcept(
        {
            "code": "204",
            "definition": "Paediatric Rehabilitation Medicine",
            "display": "Paediatric Rehabilitation Medicine",
        }
    )
    """
    Paediatric Rehabilitation Medicine

    Paediatric Rehabilitation Medicine
    """

    two05 = CodeSystemConcept(
        {
            "code": "205",
            "definition": "Paediatric Rheumatology",
            "display": "Paediatric Rheumatology",
        }
    )
    """
    Paediatric Rheumatology

    Paediatric Rheumatology
    """

    two06 = CodeSystemConcept(
        {
            "code": "206",
            "definition": "Paediatric Sleep Medicine",
            "display": "Paediatric Sleep Medicine",
        }
    )
    """
    Paediatric Sleep Medicine

    Paediatric Sleep Medicine
    """

    two07 = CodeSystemConcept(
        {
            "code": "207",
            "definition": "Paediatric Surgery",
            "display": "Paediatric Surgery",
        }
    )
    """
    Paediatric Surgery

    Paediatric Surgery
    """

    two08 = CodeSystemConcept(
        {
            "code": "208",
            "definition": "Paediatric Thoracic Medicine",
            "display": "Paediatric Thoracic Medicine",
        }
    )
    """
    Paediatric Thoracic Medicine

    Paediatric Thoracic Medicine
    """

    two09 = CodeSystemConcept(
        {
            "code": "209",
            "definition": "Diagnostic Radiology/Xray/CT/Fluoroscopy",
            "display": "Diag. Radiology /Xray /CT /Fluoroscopy",
        }
    )
    """
    Diag. Radiology /Xray /CT /Fluoroscopy

    Diagnostic Radiology/Xray/CT/Fluoroscopy
    """

    two10 = CodeSystemConcept(
        {
            "code": "210",
            "definition": "Diagnostic Ultrasound",
            "display": "Diagnostic Ultrasound",
        }
    )
    """
    Diagnostic Ultrasound

    Diagnostic Ultrasound
    """

    two11 = CodeSystemConcept(
        {
            "code": "211",
            "definition": "Magnetic Resonance Imaging (MRI)",
            "display": "Magnetic Resonance Imaging (MRI)",
        }
    )
    """
    Magnetic Resonance Imaging (MRI)

    Magnetic Resonance Imaging (MRI)
    """

    two12 = CodeSystemConcept(
        {"code": "212", "definition": "Nuclear Medicine", "display": "Nuclear Medicine"}
    )
    """
    Nuclear Medicine

    Nuclear Medicine
    """

    two13 = CodeSystemConcept(
        {
            "code": "213",
            "definition": "Obstetric & Gynaecological Ultrasound",
            "display": "Obstetric/Gynaecological Ultrasound",
        }
    )
    """
    Obstetric/Gynaecological Ultrasound

    Obstetric & Gynaecological Ultrasound
    """

    two14 = CodeSystemConcept(
        {
            "code": "214",
            "definition": "Radiation oncology",
            "display": "Radiation Oncology",
        }
    )
    """
    Radiation Oncology

    Radiation oncology
    """

    two15 = CodeSystemConcept(
        {
            "code": "215",
            "definition": "Cardiothoracic surgery",
            "display": "Cardiothoracic Surgery",
        }
    )
    """
    Cardiothoracic Surgery

    Cardiothoracic surgery
    """

    two16 = CodeSystemConcept(
        {"code": "216", "definition": "Neurosurgery", "display": "Neurosurgery"}
    )
    """
    Neurosurgery

    Neurosurgery
    """

    two17 = CodeSystemConcept(
        {"code": "217", "definition": "Ophthalmology", "display": "Ophthalmology"}
    )
    """
    Ophthalmology

    Ophthalmology
    """

    two18 = CodeSystemConcept(
        {
            "code": "218",
            "definition": "Orthopaedic surgery",
            "display": "Orthopaedic Surgery",
        }
    )
    """
    Orthopaedic Surgery

    Orthopaedic surgery
    """

    two19 = CodeSystemConcept(
        {
            "code": "219",
            "definition": "Otolaryngology - Head & Neck Surgery",
            "display": "Otolaryngology/Head & Neck Surgery",
        }
    )
    """
    Otolaryngology/Head & Neck Surgery

    Otolaryngology - Head & Neck Surgery
    """

    two20 = CodeSystemConcept(
        {
            "code": "220",
            "definition": "Plastic & Reconstructive Surgery",
            "display": "Plastic & Reconstructive Surgery",
        }
    )
    """
    Plastic & Reconstructive Surgery

    Plastic & Reconstructive Surgery
    """

    two21 = CodeSystemConcept(
        {
            "code": "221",
            "definition": "Surgery - General",
            "display": "Surgery - General",
        }
    )
    """
    Surgery - General

    Surgery - General
    """

    two22 = CodeSystemConcept(
        {"code": "222", "definition": "Urology", "display": "Urology"}
    )
    """
    Urology

    Urology
    """

    two23 = CodeSystemConcept(
        {"code": "223", "definition": "Vascular surgery", "display": "Vascular Surgery"}
    )
    """
    Vascular Surgery

    Vascular surgery
    """

    two24 = CodeSystemConcept(
        {"code": "224", "definition": "Support groups", "display": "Support Groups"}
    )
    """
    Support Groups

    Support groups
    """

    two25 = CodeSystemConcept(
        {"code": "225", "definition": "Air ambulance", "display": "Air ambulance"}
    )
    """
    Air ambulance

    Air ambulance
    """

    two26 = CodeSystemConcept(
        {"code": "226", "definition": "Ambulance", "display": "Ambulance"}
    )
    """
    Ambulance

    Ambulance
    """

    two27 = CodeSystemConcept(
        {"code": "227", "definition": "Blood transport", "display": "Blood Transport"}
    )
    """
    Blood Transport

    Blood transport
    """

    two28 = CodeSystemConcept(
        {"code": "228", "definition": "Community bus", "display": "Community Bus"}
    )
    """
    Community Bus

    Community bus
    """

    two29 = CodeSystemConcept(
        {
            "code": "229",
            "definition": "Flying doctor service",
            "display": "Flying Doctor Service",
        }
    )
    """
    Flying Doctor Service

    Flying doctor service
    """

    two30 = CodeSystemConcept(
        {
            "code": "230",
            "definition": "Patient transport",
            "display": "Patient Transport",
        }
    )
    """
    Patient Transport

    Patient transport
    """

    two31 = CodeSystemConcept({"code": "231", "definition": "A&E", "display": "A&E"})
    """
    A&E

    A&E
    """

    two32 = CodeSystemConcept({"code": "232", "definition": "A&EP", "display": "A&EP"})
    """
    A&EP

    A&EP
    """

    two33 = CodeSystemConcept(
        {"code": "233", "definition": "Abuse", "display": "Abuse"}
    )
    """
    Abuse

    Abuse
    """

    two34 = CodeSystemConcept({"code": "234", "definition": "ACAS", "display": "ACAS"})
    """
    ACAS

    ACAS
    """

    two35 = CodeSystemConcept(
        {"code": "235", "definition": "Access", "display": "Access"}
    )
    """
    Access

    Access
    """

    two36 = CodeSystemConcept(
        {"code": "236", "definition": "Accident", "display": "Accident"}
    )
    """
    Accident

    Accident
    """

    two37 = CodeSystemConcept(
        {
            "code": "237",
            "definition": "Acute Inpatient Service's",
            "display": "Acute Inpatient Serv",
        }
    )
    """
    Acute Inpatient Serv

    Acute Inpatient Service's
    """

    two38 = CodeSystemConcept(
        {
            "code": "238",
            "definition": "Adult Day Programs",
            "display": "Adult Day Programs",
        }
    )
    """
    Adult Day Programs

    Adult Day Programs
    """

    two39 = CodeSystemConcept(
        {
            "code": "239",
            "definition": "Adult Mental Health Services",
            "display": "Adult Mental Health Services",
        }
    )
    """
    Adult Mental Health Services

    Adult Mental Health Services
    """

    two40 = CodeSystemConcept(
        {"code": "240", "definition": "Advice", "display": "Advice"}
    )
    """
    Advice

    Advice
    """

    two41 = CodeSystemConcept(
        {"code": "241", "definition": "Advocacy", "display": "Advocacy"}
    )
    """
    Advocacy

    Advocacy
    """

    two42 = CodeSystemConcept(
        {
            "code": "242",
            "definition": "Aged Persons Mental Health Residential Units",
            "display": "Aged Persons Mental ",
        }
    )
    """
    Aged Persons Mental 

    Aged Persons Mental Health Residential Units
    """

    two43 = CodeSystemConcept(
        {
            "code": "243",
            "definition": "Aged Persons Mental Health Services",
            "display": "Aged Persons Mental ",
        }
    )
    """
    Aged Persons Mental 

    Aged Persons Mental Health Services
    """

    two44 = CodeSystemConcept(
        {
            "code": "244",
            "definition": "Aged Persons Mental Health Teams",
            "display": "Aged Persons Mental ",
        }
    )
    """
    Aged Persons Mental 

    Aged Persons Mental Health Teams
    """

    two45 = CodeSystemConcept({"code": "245", "definition": "Aids", "display": "Aids"})
    """
    Aids

    Aids
    """

    two46 = CodeSystemConcept(
        {"code": "246", "definition": "Al-Anon", "display": "Al-Anon"}
    )
    """
    Al-Anon

    Al-Anon
    """

    two47 = CodeSystemConcept(
        {"code": "247", "definition": "Alcohol", "display": "Alcohol"}
    )
    """
    Alcohol

    Alcohol
    """

    two48 = CodeSystemConcept(
        {"code": "248", "definition": "Al-Teen", "display": "Al-Teen"}
    )
    """
    Al-Teen

    Al-Teen
    """

    two49 = CodeSystemConcept(
        {"code": "249", "definition": "Antenatal", "display": "Antenatal"}
    )
    """
    Antenatal

    Antenatal
    """

    two50 = CodeSystemConcept(
        {"code": "250", "definition": "Anxiety", "display": "Anxiety"}
    )
    """
    Anxiety

    Anxiety
    """

    two51 = CodeSystemConcept(
        {"code": "251", "definition": "Arthritis", "display": "Arthritis"}
    )
    """
    Arthritis

    Arthritis
    """

    two52 = CodeSystemConcept(
        {"code": "252", "definition": "Assessment", "display": "Assessment"}
    )
    """
    Assessment

    Assessment
    """

    two53 = CodeSystemConcept(
        {"code": "253", "definition": "Assistance", "display": "Assistance"}
    )
    """
    Assistance

    Assistance
    """

    two54 = CodeSystemConcept(
        {"code": "254", "definition": "Asthma", "display": "Asthma"}
    )
    """
    Asthma

    Asthma
    """

    two55 = CodeSystemConcept({"code": "255", "definition": "ATSS", "display": "ATSS"})
    """
    ATSS

    ATSS
    """

    two56 = CodeSystemConcept(
        {"code": "256", "definition": "Attendant Care", "display": "Attendant Care"}
    )
    """
    Attendant Care

    Attendant Care
    """

    two57 = CodeSystemConcept(
        {"code": "257", "definition": "Babies", "display": "Babies"}
    )
    """
    Babies

    Babies
    """

    two58 = CodeSystemConcept(
        {
            "code": "258",
            "definition": "Bathroom Modification",
            "display": "Bathroom Modificatio",
        }
    )
    """
    Bathroom Modificatio

    Bathroom Modification
    """

    two59 = CodeSystemConcept(
        {"code": "259", "definition": "Behavior", "display": "Behavior"}
    )
    """
    Behavior

    Behavior
    """

    two60 = CodeSystemConcept(
        {
            "code": "260",
            "definition": "Behavior Intervention",
            "display": "Behavior Interventi",
        }
    )
    """
    Behavior Interventi

    Behavior Intervention
    """

    two61 = CodeSystemConcept(
        {"code": "261", "definition": "Bereavement", "display": "Bereavement"}
    )
    """
    Bereavement

    Bereavement
    """

    two62 = CodeSystemConcept(
        {"code": "262", "definition": "Bipolar", "display": "Bipolar"}
    )
    """
    Bipolar

    Bipolar
    """

    two63 = CodeSystemConcept(
        {"code": "263", "definition": "Birth", "display": "Birth"}
    )
    """
    Birth

    Birth
    """

    two64 = CodeSystemConcept(
        {"code": "264", "definition": "Birth Control", "display": "Birth Control"}
    )
    """
    Birth Control

    Birth Control
    """

    two65 = CodeSystemConcept(
        {"code": "265", "definition": "Birthing Options", "display": "Birthing Options"}
    )
    """
    Birthing Options

    Birthing Options
    """

    two66 = CodeSystemConcept({"code": "266", "definition": "BIST", "display": "BIST"})
    """
    BIST

    BIST
    """

    two67 = CodeSystemConcept(
        {"code": "267", "definition": "Blood", "display": "Blood"}
    )
    """
    Blood

    Blood
    """

    two68 = CodeSystemConcept({"code": "268", "definition": "Bone", "display": "Bone"})
    """
    Bone

    Bone
    """

    two69 = CodeSystemConcept(
        {"code": "269", "definition": "Bowel", "display": "Bowel"}
    )
    """
    Bowel

    Bowel
    """

    two70 = CodeSystemConcept(
        {"code": "270", "definition": "Brain", "display": "Brain"}
    )
    """
    Brain

    Brain
    """

    two71 = CodeSystemConcept(
        {"code": "271", "definition": "Breast Feeding", "display": "Breast Feeding"}
    )
    """
    Breast Feeding

    Breast Feeding
    """

    two72 = CodeSystemConcept(
        {"code": "272", "definition": "Breast Screen", "display": "Breast Screen"}
    )
    """
    Breast Screen

    Breast Screen
    """

    two73 = CodeSystemConcept(
        {"code": "273", "definition": "Brokerage", "display": "Brokerage"}
    )
    """
    Brokerage

    Brokerage
    """

    two74 = CodeSystemConcept(
        {"code": "274", "definition": "Cancer", "display": "Cancer"}
    )
    """
    Cancer

    Cancer
    """

    two75 = CodeSystemConcept(
        {"code": "275", "definition": "Cancer Support", "display": "Cancer Support"}
    )
    """
    Cancer Support

    Cancer Support
    """

    two76 = CodeSystemConcept(
        {
            "code": "276",
            "definition": "Cardiovascular Disease",
            "display": "Cardiovascular Disea",
        }
    )
    """
    Cardiovascular Disea

    Cardiovascular Disease
    """

    two77 = CodeSystemConcept(
        {"code": "277", "definition": "Care Packages", "display": "Care Packages"}
    )
    """
    Care Packages

    Care Packages
    """

    two78 = CodeSystemConcept(
        {"code": "278", "definition": "Carer", "display": "Carer"}
    )
    """
    Carer

    Carer
    """

    two79 = CodeSystemConcept(
        {"code": "279", "definition": "Case Management", "display": "Case Management"}
    )
    """
    Case Management

    Case Management
    """

    two80 = CodeSystemConcept(
        {"code": "280", "definition": "Casualty", "display": "Casualty"}
    )
    """
    Casualty

    Casualty
    """

    two81 = CodeSystemConcept(
        {"code": "281", "definition": "Centrelink", "display": "Centrelink"}
    )
    """
    Centrelink

    Centrelink
    """

    two82 = CodeSystemConcept(
        {"code": "282", "definition": "Chemists", "display": "Chemists"}
    )
    """
    Chemists

    Chemists
    """

    two83 = CodeSystemConcept(
        {
            "code": "283",
            "definition": "Child And Adolescent Mental Health Services",
            "display": "Child And Adolescent",
        }
    )
    """
    Child And Adolescent

    Child And Adolescent Mental Health Services
    """

    two84 = CodeSystemConcept(
        {"code": "284", "definition": "Child Care", "display": "Child Care"}
    )
    """
    Child Care

    Child Care
    """

    two85 = CodeSystemConcept(
        {"code": "285", "definition": "Child Services", "display": "Child Services"}
    )
    """
    Child Services

    Child Services
    """

    two86 = CodeSystemConcept(
        {"code": "286", "definition": "Children", "display": "Children"}
    )
    """
    Children

    Children
    """

    two87 = CodeSystemConcept(
        {
            "code": "287",
            "definition": "Children's Services",
            "display": "Children's Services",
        }
    )
    """
    Children's Services

    Children's Services
    """

    two88 = CodeSystemConcept(
        {"code": "288", "definition": "Cholesterol", "display": "Cholesterol"}
    )
    """
    Cholesterol

    Cholesterol
    """

    two89 = CodeSystemConcept(
        {"code": "289", "definition": "Clothing", "display": "Clothing"}
    )
    """
    Clothing

    Clothing
    """

    two90 = CodeSystemConcept(
        {
            "code": "290",
            "definition": "Community Based Accommodation",
            "display": "Community Based Acco",
        }
    )
    """
    Community Based Acco

    Community Based Accommodation
    """

    two91 = CodeSystemConcept(
        {
            "code": "291",
            "definition": "Community Care Unit",
            "display": "Community Care Unit",
        }
    )
    """
    Community Care Unit

    Community Care Unit
    """

    two92 = CodeSystemConcept(
        {
            "code": "292",
            "definition": "Community Child And Adolescent Mental Health Services",
            "display": "Community Child And ",
        }
    )
    """
    Community Child And 

    Community Child And Adolescent Mental Health Services
    """

    two93 = CodeSystemConcept(
        {"code": "293", "definition": "Community Health", "display": "Community Health"}
    )
    """
    Community Health

    Community Health
    """

    two94 = CodeSystemConcept(
        {
            "code": "294",
            "definition": "Community Residential Unit",
            "display": "Community Residentia",
        }
    )
    """
    Community Residentia

    Community Residential Unit
    """

    two95 = CodeSystemConcept(
        {
            "code": "295",
            "definition": "Community Transport",
            "display": "Community Transport",
        }
    )
    """
    Community Transport

    Community Transport
    """

    two96 = CodeSystemConcept(
        {
            "code": "296",
            "definition": "Companion Visiting",
            "display": "Companion Visiting",
        }
    )
    """
    Companion Visiting

    Companion Visiting
    """

    two97 = CodeSystemConcept(
        {"code": "297", "definition": "Companionship", "display": "Companionship"}
    )
    """
    Companionship

    Companionship
    """

    two98 = CodeSystemConcept(
        {"code": "298", "definition": "Consumer Advice", "display": "Consumer Advice"}
    )
    """
    Consumer Advice

    Consumer Advice
    """

    two99 = CodeSystemConcept(
        {"code": "299", "definition": "Consumer Issues", "display": "Consumer Issues"}
    )
    """
    Consumer Issues

    Consumer Issues
    """

    three00 = CodeSystemConcept(
        {
            "code": "300",
            "definition": "Continuing Care Services",
            "display": "Continuing Care Serv",
        }
    )
    """
    Continuing Care Serv

    Continuing Care Services
    """

    three01 = CodeSystemConcept(
        {
            "code": "301",
            "definition": "Contraception Information",
            "display": "Contraception Inform",
        }
    )
    """
    Contraception Inform

    Contraception Information
    """

    three02 = CodeSystemConcept(
        {
            "code": "302",
            "definition": "Coordinating Bodies",
            "display": "Coordinating Bodies",
        }
    )
    """
    Coordinating Bodies

    Coordinating Bodies
    """

    three03 = CodeSystemConcept(
        {
            "code": "303",
            "definition": "Correctional Services",
            "display": "Correctional Service",
        }
    )
    """
    Correctional Service

    Correctional Services
    """

    three04 = CodeSystemConcept(
        {
            "code": "304",
            "definition": "Council Environmental Health",
            "display": "Council Environmenta",
        }
    )
    """
    Council Environmenta

    Council Environmental Health
    """

    three05 = CodeSystemConcept(
        {"code": "305", "definition": "Counselling", "display": "Counselling"}
    )
    """
    Counselling

    Counselling
    """

    three06 = CodeSystemConcept(
        {"code": "306", "definition": "Criminal", "display": "Criminal"}
    )
    """
    Criminal

    Criminal
    """

    three07 = CodeSystemConcept(
        {"code": "307", "definition": "Crises", "display": "Crises"}
    )
    """
    Crises

    Crises
    """

    three08 = CodeSystemConcept(
        {
            "code": "308",
            "definition": "Crisis Assessment And Treatment Services (Cats)",
            "display": "Crisis Assessment An",
        }
    )
    """
    Crisis Assessment An

    Crisis Assessment And Treatment Services (Cats)
    """

    three09 = CodeSystemConcept(
        {
            "code": "309",
            "definition": "Crisis Assistance",
            "display": "Crisis Assistance",
        }
    )
    """
    Crisis Assistance

    Crisis Assistance
    """

    three10 = CodeSystemConcept(
        {"code": "310", "definition": "Crisis Refuge", "display": "Crisis Refuge"}
    )
    """
    Crisis Refuge

    Crisis Refuge
    """

    three11 = CodeSystemConcept(
        {"code": "311", "definition": "Day Program", "display": "Day Program"}
    )
    """
    Day Program

    Day Program
    """

    three12 = CodeSystemConcept(
        {"code": "312", "definition": "Deaf", "display": "Deaf"}
    )
    """
    Deaf

    Deaf
    """

    three13 = CodeSystemConcept(
        {"code": "313", "definition": "Dental Hygiene", "display": "Dental Hygiene"}
    )
    """
    Dental Hygiene

    Dental Hygiene
    """

    three14 = CodeSystemConcept(
        {"code": "314", "definition": "Dentistry", "display": "Dentistry"}
    )
    """
    Dentistry

    Dentistry
    """

    three15 = CodeSystemConcept(
        {"code": "315", "definition": "Dentures", "display": "Dentures"}
    )
    """
    Dentures

    Dentures
    """

    three16 = CodeSystemConcept(
        {"code": "316", "definition": "Depression", "display": "Depression"}
    )
    """
    Depression

    Depression
    """

    three17 = CodeSystemConcept(
        {"code": "317", "definition": "Detoxification", "display": "Detoxification"}
    )
    """
    Detoxification

    Detoxification
    """

    three18 = CodeSystemConcept(
        {"code": "318", "definition": "Diabetes", "display": "Diabetes"}
    )
    """
    Diabetes

    Diabetes
    """

    three19 = CodeSystemConcept(
        {
            "code": "319",
            "definition": "Diaphragm Fitting",
            "display": "Diaphragm Fitting",
        }
    )
    """
    Diaphragm Fitting

    Diaphragm Fitting
    """

    three20 = CodeSystemConcept(
        {"code": "320", "definition": "Dieticians", "display": "Dieticians"}
    )
    """
    Dieticians

    Dieticians
    """

    three21 = CodeSystemConcept(
        {"code": "321", "definition": "Disabled Parking", "display": "Disabled Parking"}
    )
    """
    Disabled Parking

    Disabled Parking
    """

    three22 = CodeSystemConcept(
        {"code": "322", "definition": "District Nursing", "display": "District Nursing"}
    )
    """
    District Nursing

    District Nursing
    """

    three23 = CodeSystemConcept(
        {"code": "323", "definition": "Divorce", "display": "Divorce"}
    )
    """
    Divorce

    Divorce
    """

    three24 = CodeSystemConcept(
        {"code": "324", "definition": "Doctors", "display": "Doctors"}
    )
    """
    Doctors

    Doctors
    """

    three25 = CodeSystemConcept(
        {"code": "325", "definition": "Drink-Drive", "display": "Drink-Drive"}
    )
    """
    Drink-Drive

    Drink-Drive
    """

    three26 = CodeSystemConcept(
        {
            "code": "326",
            "definition": "Dual Diagnosis Services",
            "display": "Dual Diagnosis Servi",
        }
    )
    """
    Dual Diagnosis Servi

    Dual Diagnosis Services
    """

    three27 = CodeSystemConcept(
        {"code": "327", "definition": "Early Choice", "display": "Early Choice"}
    )
    """
    Early Choice

    Early Choice
    """

    three28 = CodeSystemConcept(
        {"code": "328", "definition": "Eating Disorder", "display": "Eating Disorder"}
    )
    """
    Eating Disorder

    Eating Disorder
    """

    three30 = CodeSystemConcept(
        {"code": "330", "definition": "Emergency Relief", "display": "Emergency Relief"}
    )
    """
    Emergency Relief

    Emergency Relief
    """

    three31 = CodeSystemConcept(
        {
            "code": "331",
            "definition": "Employment And Training",
            "display": "Employment And Train",
        }
    )
    """
    Employment And Train

    Employment And Training
    """

    three32 = CodeSystemConcept(
        {"code": "332", "definition": "Environment", "display": "Environment"}
    )
    """
    Environment

    Environment
    """

    three33 = CodeSystemConcept(
        {"code": "333", "definition": "Equipment", "display": "Equipment"}
    )
    """
    Equipment

    Equipment
    """

    three34 = CodeSystemConcept(
        {"code": "334", "definition": "Exercise", "display": "Exercise"}
    )
    """
    Exercise

    Exercise
    """

    three35 = CodeSystemConcept(
        {"code": "335", "definition": "Facility", "display": "Facility"}
    )
    """
    Facility

    Facility
    """

    three36 = CodeSystemConcept(
        {"code": "336", "definition": "Family Choice", "display": "Family Choice"}
    )
    """
    Family Choice

    Family Choice
    """

    three37 = CodeSystemConcept(
        {"code": "337", "definition": "Family Law", "display": "Family Law"}
    )
    """
    Family Law

    Family Law
    """

    three38 = CodeSystemConcept(
        {"code": "338", "definition": "Family Options", "display": "Family Options"}
    )
    """
    Family Options

    Family Options
    """

    three39 = CodeSystemConcept(
        {"code": "339", "definition": "Family Services", "display": "Family Services"}
    )
    """
    Family Services

    Family Services
    """

    three40 = CodeSystemConcept(
        {"code": "340", "definition": "FFYA", "display": "FFYA"}
    )
    """
    FFYA

    FFYA
    """

    three41 = CodeSystemConcept(
        {"code": "341", "definition": "Financial Aid", "display": "Financial Aid"}
    )
    """
    Financial Aid

    Financial Aid
    """

    three42 = CodeSystemConcept(
        {"code": "342", "definition": "Fitness", "display": "Fitness"}
    )
    """
    Fitness

    Fitness
    """

    three43 = CodeSystemConcept(
        {
            "code": "343",
            "definition": "Flexible Care Packages",
            "display": "Flexible Care Packag",
        }
    )
    """
    Flexible Care Packag

    Flexible Care Packages
    """

    three44 = CodeSystemConcept(
        {"code": "344", "definition": "Food", "display": "Food"}
    )
    """
    Food

    Food
    """

    three45 = CodeSystemConcept(
        {"code": "345", "definition": "Food Vouchers", "display": "Food Vouchers"}
    )
    """
    Food Vouchers

    Food Vouchers
    """

    three46 = CodeSystemConcept(
        {
            "code": "346",
            "definition": "Forensic Mental Health Services",
            "display": "Forensic Mental Heal",
        }
    )
    """
    Forensic Mental Heal

    Forensic Mental Health Services
    """

    three47 = CodeSystemConcept(
        {"code": "347", "definition": "Futures", "display": "Futures"}
    )
    """
    Futures

    Futures
    """

    three48 = CodeSystemConcept(
        {
            "code": "348",
            "definition": "Futures For Young Adults",
            "display": "Futures For Young Ad",
        }
    )
    """
    Futures For Young Ad

    Futures For Young Adults
    """

    three49 = CodeSystemConcept(
        {
            "code": "349",
            "definition": "General Practitioners",
            "display": "General Practitioner",
        }
    )
    """
    General Practitioner

    General Practitioners
    """

    three50 = CodeSystemConcept(
        {"code": "350", "definition": "Grants", "display": "Grants"}
    )
    """
    Grants

    Grants
    """

    three51 = CodeSystemConcept(
        {"code": "351", "definition": "Grief", "display": "Grief"}
    )
    """
    Grief

    Grief
    """

    three52 = CodeSystemConcept(
        {
            "code": "352",
            "definition": "Grief Counselling",
            "display": "Grief Counselling",
        }
    )
    """
    Grief Counselling

    Grief Counselling
    """

    three53 = CodeSystemConcept(
        {"code": "353", "definition": "HACC", "display": "HACC"}
    )
    """
    HACC

    HACC
    """

    three54 = CodeSystemConcept(
        {"code": "354", "definition": "Heart Disease", "display": "Heart Disease"}
    )
    """
    Heart Disease

    Heart Disease
    """

    three55 = CodeSystemConcept(
        {"code": "355", "definition": "Help", "display": "Help"}
    )
    """
    Help

    Help
    """

    three56 = CodeSystemConcept(
        {
            "code": "356",
            "definition": "High Blood Pressure",
            "display": "High Blood Pressure",
        }
    )
    """
    High Blood Pressure

    High Blood Pressure
    """

    three57 = CodeSystemConcept(
        {"code": "357", "definition": "Home Help", "display": "Home Help"}
    )
    """
    Home Help

    Home Help
    """

    three58 = CodeSystemConcept(
        {"code": "358", "definition": "Home Nursing", "display": "Home Nursing"}
    )
    """
    Home Nursing

    Home Nursing
    """

    three59 = CodeSystemConcept(
        {"code": "359", "definition": "Homefirst", "display": "Homefirst"}
    )
    """
    Homefirst

    Homefirst
    """

    three60 = CodeSystemConcept(
        {"code": "360", "definition": "Hospice Care", "display": "Hospice Care"}
    )
    """
    Hospice Care

    Hospice Care
    """

    three61 = CodeSystemConcept(
        {
            "code": "361",
            "definition": "Hospital Services",
            "display": "Hospital Services",
        }
    )
    """
    Hospital Services

    Hospital Services
    """

    three62 = CodeSystemConcept(
        {"code": "362", "definition": "Hospital To Home", "display": "Hospital To Home"}
    )
    """
    Hospital To Home

    Hospital To Home
    """

    three64 = CodeSystemConcept(
        {"code": "364", "definition": "Hostel", "display": "Hostel"}
    )
    """
    Hostel

    Hostel
    """

    three65 = CodeSystemConcept(
        {
            "code": "365",
            "definition": "Hostel Accommodation",
            "display": "Hostel Accommodation",
        }
    )
    """
    Hostel Accommodation

    Hostel Accommodation
    """

    three66 = CodeSystemConcept(
        {"code": "366", "definition": "Household Items", "display": "Household Items"}
    )
    """
    Household Items

    Household Items
    """

    three67 = CodeSystemConcept(
        {"code": "367", "definition": "Hypertension", "display": "Hypertension"}
    )
    """
    Hypertension

    Hypertension
    """

    three68 = CodeSystemConcept(
        {"code": "368", "definition": "Illness", "display": "Illness"}
    )
    """
    Illness

    Illness
    """

    three69 = CodeSystemConcept(
        {
            "code": "369",
            "definition": "Independent Living",
            "display": "Independent Living",
        }
    )
    """
    Independent Living

    Independent Living
    """

    three70 = CodeSystemConcept(
        {"code": "370", "definition": "Information", "display": "Information"}
    )
    """
    Information

    Information
    """

    three71 = CodeSystemConcept(
        {"code": "371", "definition": "Injury", "display": "Injury"}
    )
    """
    Injury

    Injury
    """

    three72 = CodeSystemConcept(
        {"code": "372", "definition": "Intake", "display": "Intake"}
    )
    """
    Intake

    Intake
    """

    three73 = CodeSystemConcept(
        {
            "code": "373",
            "definition": "Intensive Mobile Youth Outreach Services (Imyos)",
            "display": "Intensive Mobile You",
        }
    )
    """
    Intensive Mobile You

    Intensive Mobile Youth Outreach Services (Imyos)
    """

    three74 = CodeSystemConcept(
        {"code": "374", "definition": "Intervention", "display": "Intervention"}
    )
    """
    Intervention

    Intervention
    """

    three75 = CodeSystemConcept(
        {"code": "375", "definition": "Job Searching", "display": "Job Searching"}
    )
    """
    Job Searching

    Job Searching
    """

    three76 = CodeSystemConcept(
        {"code": "376", "definition": "Justice", "display": "Justice"}
    )
    """
    Justice

    Justice
    """

    three77 = CodeSystemConcept(
        {"code": "377", "definition": "Leisure", "display": "Leisure"}
    )
    """
    Leisure

    Leisure
    """

    three78 = CodeSystemConcept(
        {"code": "378", "definition": "Loans", "display": "Loans"}
    )
    """
    Loans

    Loans
    """

    three79 = CodeSystemConcept(
        {
            "code": "379",
            "definition": "Low Income Earners",
            "display": "Low Income Earners",
        }
    )
    """
    Low Income Earners

    Low Income Earners
    """

    three80 = CodeSystemConcept(
        {"code": "380", "definition": "Lung", "display": "Lung"}
    )
    """
    Lung

    Lung
    """

    three81 = CodeSystemConcept(
        {
            "code": "381",
            "definition": "Making A Difference",
            "display": "Making A Difference",
        }
    )
    """
    Making A Difference

    Making A Difference
    """

    three82 = CodeSystemConcept(
        {"code": "382", "definition": "Medical Services", "display": "Medical Services"}
    )
    """
    Medical Services

    Medical Services
    """

    three83 = CodeSystemConcept(
        {
            "code": "383",
            "definition": "Medical Specialists",
            "display": "Medical Specialists",
        }
    )
    """
    Medical Specialists

    Medical Specialists
    """

    three84 = CodeSystemConcept(
        {
            "code": "384",
            "definition": "Medication Administration",
            "display": "Medication Administr",
        }
    )
    """
    Medication Administr

    Medication Administration
    """

    three85 = CodeSystemConcept(
        {
            "code": "385",
            "definition": "Menstrual Information",
            "display": "Menstrual Informatio",
        }
    )
    """
    Menstrual Informatio

    Menstrual Information
    """

    three86 = CodeSystemConcept(
        {"code": "386", "definition": "Methadone", "display": "Methadone"}
    )
    """
    Methadone

    Methadone
    """

    three87 = CodeSystemConcept(
        {
            "code": "387",
            "definition": "Mobile Support And Treatment Services (MSTS)",
            "display": "Mobile Support And T",
        }
    )
    """
    Mobile Support And T

    Mobile Support And Treatment Services (MSTS)
    """

    three88 = CodeSystemConcept(
        {"code": "388", "definition": "Motor Neurone", "display": "Motor Neurone"}
    )
    """
    Motor Neurone

    Motor Neurone
    """

    three89 = CodeSystemConcept(
        {
            "code": "389",
            "definition": "Multiple Sclerosis",
            "display": "Multiple Sclerosis",
        }
    )
    """
    Multiple Sclerosis

    Multiple Sclerosis
    """

    three90 = CodeSystemConcept(
        {
            "code": "390",
            "definition": "Neighbourhood House",
            "display": "Neighbourhood House",
        }
    )
    """
    Neighbourhood House

    Neighbourhood House
    """

    three91 = CodeSystemConcept(
        {"code": "391", "definition": "Nursing Home", "display": "Nursing Home"}
    )
    """
    Nursing Home

    Nursing Home
    """

    three92 = CodeSystemConcept(
        {"code": "392", "definition": "Nursing Mothers", "display": "Nursing Mothers"}
    )
    """
    Nursing Mothers

    Nursing Mothers
    """

    three93 = CodeSystemConcept(
        {"code": "393", "definition": "Obesity", "display": "Obesity"}
    )
    """
    Obesity

    Obesity
    """

    three94 = CodeSystemConcept(
        {
            "code": "394",
            "definition": "Occupational Health & Safety",
            "display": "Occupational Health ",
        }
    )
    """
    Occupational Health 

    Occupational Health & Safety
    """

    three95 = CodeSystemConcept(
        {"code": "395", "definition": "Optometrist", "display": "Optometrist"}
    )
    """
    Optometrist

    Optometrist
    """

    three96 = CodeSystemConcept(
        {"code": "396", "definition": "Oral Hygiene", "display": "Oral Hygiene"}
    )
    """
    Oral Hygiene

    Oral Hygiene
    """

    three97 = CodeSystemConcept(
        {"code": "397", "definition": "Outpatients", "display": "Outpatients"}
    )
    """
    Outpatients

    Outpatients
    """

    three98 = CodeSystemConcept(
        {"code": "398", "definition": "Outreach Service", "display": "Outreach Service"}
    )
    """
    Outreach Service

    Outreach Service
    """

    three99 = CodeSystemConcept(
        {"code": "399", "definition": "PADP", "display": "PADP"}
    )
    """
    PADP

    PADP
    """

    four00 = CodeSystemConcept({"code": "400", "definition": "Pain", "display": "Pain"})
    """
    Pain

    Pain
    """

    four01 = CodeSystemConcept(
        {"code": "401", "definition": "Pap Smear", "display": "Pap Smear"}
    )
    """
    Pap Smear

    Pap Smear
    """

    four02 = CodeSystemConcept(
        {"code": "402", "definition": "Parenting", "display": "Parenting"}
    )
    """
    Parenting

    Parenting
    """

    four03 = CodeSystemConcept(
        {
            "code": "403",
            "definition": "Peak Organizations",
            "display": "Peak Organizations",
        }
    )
    """
    Peak Organizations

    Peak Organizations
    """

    four04 = CodeSystemConcept(
        {"code": "404", "definition": "Personal Care", "display": "Personal Care"}
    )
    """
    Personal Care

    Personal Care
    """

    four05 = CodeSystemConcept(
        {"code": "405", "definition": "Pharmacies", "display": "Pharmacies"}
    )
    """
    Pharmacies

    Pharmacies
    """

    four06 = CodeSystemConcept(
        {"code": "406", "definition": "Phobias", "display": "Phobias"}
    )
    """
    Phobias

    Phobias
    """

    four07 = CodeSystemConcept(
        {"code": "407", "definition": "Physical", "display": "Physical"}
    )
    """
    Physical

    Physical
    """

    four08 = CodeSystemConcept(
        {
            "code": "408",
            "definition": "Physical Activity",
            "display": "Physical Activity",
        }
    )
    """
    Physical Activity

    Physical Activity
    """

    four09 = CodeSystemConcept(
        {"code": "409", "definition": "Postnatal", "display": "Postnatal"}
    )
    """
    Postnatal

    Postnatal
    """

    four10 = CodeSystemConcept(
        {"code": "410", "definition": "Pregnancy", "display": "Pregnancy"}
    )
    """
    Pregnancy

    Pregnancy
    """

    four11 = CodeSystemConcept(
        {"code": "411", "definition": "Pregnancy Tests", "display": "Pregnancy Tests"}
    )
    """
    Pregnancy Tests

    Pregnancy Tests
    """

    four12 = CodeSystemConcept(
        {"code": "412", "definition": "Preschool", "display": "Preschool"}
    )
    """
    Preschool

    Preschool
    """

    four13 = CodeSystemConcept(
        {"code": "413", "definition": "Prescriptions", "display": "Prescriptions"}
    )
    """
    Prescriptions

    Prescriptions
    """

    four14 = CodeSystemConcept(
        {
            "code": "414",
            "definition": "Primary Mental Health And Early Intervention Teams",
            "display": "Primary Mental Healt",
        }
    )
    """
    Primary Mental Healt

    Primary Mental Health And Early Intervention Teams
    """

    four15 = CodeSystemConcept(
        {
            "code": "415",
            "definition": "Property Maintenance",
            "display": "Property Maintenance",
        }
    )
    """
    Property Maintenance

    Property Maintenance
    """

    four16 = CodeSystemConcept(
        {"code": "416", "definition": "Prostate", "display": "Prostate"}
    )
    """
    Prostate

    Prostate
    """

    four17 = CodeSystemConcept(
        {"code": "417", "definition": "Psychiatric", "display": "Psychiatric"}
    )
    """
    Psychiatric

    Psychiatric
    """

    four18 = CodeSystemConcept(
        {
            "code": "418",
            "definition": "Psychiatric Disability Support Services - Home-Based Outreach",
            "display": "Psychiatric Disabili",
        }
    )
    """
    Psychiatric Disabili

    Psychiatric Disability Support Services - Home-Based Outreach
    """

    four19 = CodeSystemConcept(
        {
            "code": "419",
            "definition": "Psychiatric Disability Support Services - Planned Respite",
            "display": "Psychiatric Disabili",
        }
    )
    """
    Psychiatric Disabili

    Psychiatric Disability Support Services - Planned Respite
    """

    four20 = CodeSystemConcept(
        {
            "code": "420",
            "definition": "Psychiatric Disability Support Services - Residential Rehabilitation",
            "display": "Psychiatric Disabili",
        }
    )
    """
    Psychiatric Disabili

    Psychiatric Disability Support Services - Residential Rehabilitation
    """

    four21 = CodeSystemConcept(
        {
            "code": "421",
            "definition": "Psychiatric Disability Support Services Home-Based Outreach",
            "display": "Psychiatric Disabili",
        }
    )
    """
    Psychiatric Disabili

    Psychiatric Disability Support Services Home-Based Outreach
    """

    four22 = CodeSystemConcept(
        {
            "code": "422",
            "definition": "Psychiatric Disability Support Services Mutual Support And Self Help",
            "display": "Psychiatric Disabili",
        }
    )
    """
    Psychiatric Disabili

    Psychiatric Disability Support Services Mutual Support And Self Help
    """

    four23 = CodeSystemConcept(
        {
            "code": "423",
            "definition": "Psychiatric Support",
            "display": "Psychiatric Support",
        }
    )
    """
    Psychiatric Support

    Psychiatric Support
    """

    four24 = CodeSystemConcept(
        {"code": "424", "definition": "Recreation", "display": "Recreation"}
    )
    """
    Recreation

    Recreation
    """

    four25 = CodeSystemConcept(
        {"code": "425", "definition": "Referral", "display": "Referral"}
    )
    """
    Referral

    Referral
    """

    four26 = CodeSystemConcept(
        {"code": "426", "definition": "Refuge", "display": "Refuge"}
    )
    """
    Refuge

    Refuge
    """

    four27 = CodeSystemConcept(
        {"code": "427", "definition": "Rent Assistance", "display": "Rent Assistance"}
    )
    """
    Rent Assistance

    Rent Assistance
    """

    four28 = CodeSystemConcept(
        {
            "code": "428",
            "definition": "Residential Facilities",
            "display": "Residential Faciliti",
        }
    )
    """
    Residential Faciliti

    Residential Facilities
    """

    four29 = CodeSystemConcept(
        {
            "code": "429",
            "definition": "Residential Respite",
            "display": "Residential Respite",
        }
    )
    """
    Residential Respite

    Residential Respite
    """

    four30 = CodeSystemConcept(
        {"code": "430", "definition": "Respiratory", "display": "Respiratory"}
    )
    """
    Respiratory

    Respiratory
    """

    four31 = CodeSystemConcept(
        {"code": "431", "definition": "Response", "display": "Response"}
    )
    """
    Response

    Response
    """

    four32 = CodeSystemConcept(
        {"code": "432", "definition": "Rooming Houses", "display": "Rooming Houses"}
    )
    """
    Rooming Houses

    Rooming Houses
    """

    four33 = CodeSystemConcept(
        {"code": "433", "definition": "Safe Sex", "display": "Safe Sex"}
    )
    """
    Safe Sex

    Safe Sex
    """

    four34 = CodeSystemConcept(
        {
            "code": "434",
            "definition": "Secure Extended Care Inpatient Services",
            "display": "Secure Extended Care",
        }
    )
    """
    Secure Extended Care

    Secure Extended Care Inpatient Services
    """

    four35 = CodeSystemConcept(
        {"code": "435", "definition": "Self Help", "display": "Self Help"}
    )
    """
    Self Help

    Self Help
    """

    four36 = CodeSystemConcept(
        {"code": "436", "definition": "Separation", "display": "Separation"}
    )
    """
    Separation

    Separation
    """

    four37 = CodeSystemConcept(
        {"code": "437", "definition": "Services", "display": "Services"}
    )
    """
    Services

    Services
    """

    four38 = CodeSystemConcept(
        {"code": "438", "definition": "Sex Education", "display": "Sex Education"}
    )
    """
    Sex Education

    Sex Education
    """

    four39 = CodeSystemConcept(
        {"code": "439", "definition": "Sexual Abuse", "display": "Sexual Abuse"}
    )
    """
    Sexual Abuse

    Sexual Abuse
    """

    four40 = CodeSystemConcept(
        {"code": "440", "definition": "Sexual Issues", "display": "Sexual Issues"}
    )
    """
    Sexual Issues

    Sexual Issues
    """

    four41 = CodeSystemConcept(
        {
            "code": "441",
            "definition": "Sexually Transmitted Diseases",
            "display": "Sexually Transmitted",
        }
    )
    """
    Sexually Transmitted

    Sexually Transmitted Diseases
    """

    four42 = CodeSystemConcept({"code": "442", "definition": "SIDS", "display": "SIDS"})
    """
    SIDS

    SIDS
    """

    four43 = CodeSystemConcept(
        {"code": "443", "definition": "Social Support", "display": "Social Support"}
    )
    """
    Social Support

    Social Support
    """

    four44 = CodeSystemConcept(
        {"code": "444", "definition": "Socialisation", "display": "Socialisation"}
    )
    """
    Socialisation

    Socialisation
    """

    four45 = CodeSystemConcept(
        {"code": "445", "definition": "Special Needs", "display": "Special Needs"}
    )
    """
    Special Needs

    Special Needs
    """

    four46 = CodeSystemConcept(
        {"code": "446", "definition": "Speech Therapist", "display": "Speech Therapist"}
    )
    """
    Speech Therapist

    Speech Therapist
    """

    four47 = CodeSystemConcept(
        {"code": "447", "definition": "Splinting", "display": "Splinting"}
    )
    """
    Splinting

    Splinting
    """

    four48 = CodeSystemConcept(
        {"code": "448", "definition": "Sport", "display": "Sport"}
    )
    """
    Sport

    Sport
    """

    four49 = CodeSystemConcept(
        {
            "code": "449",
            "definition": "Statewide And Specialist Services",
            "display": "Statewide And Specia",
        }
    )
    """
    Statewide And Specia

    Statewide And Specialist Services
    """

    four50 = CodeSystemConcept({"code": "450", "definition": "STD", "display": "STD"})
    """
    STD

    STD
    """

    four51 = CodeSystemConcept({"code": "451", "definition": "STI", "display": "STI"})
    """
    STI

    STI
    """

    four52 = CodeSystemConcept(
        {"code": "452", "definition": "Stillbirth", "display": "Stillbirth"}
    )
    """
    Stillbirth

    Stillbirth
    """

    four53 = CodeSystemConcept(
        {"code": "453", "definition": "Stomal Care", "display": "Stomal Care"}
    )
    """
    Stomal Care

    Stomal Care
    """

    four54 = CodeSystemConcept(
        {"code": "454", "definition": "Stroke", "display": "Stroke"}
    )
    """
    Stroke

    Stroke
    """

    four55 = CodeSystemConcept(
        {"code": "455", "definition": "Substance Abuse", "display": "Substance Abuse"}
    )
    """
    Substance Abuse

    Substance Abuse
    """

    four56 = CodeSystemConcept(
        {"code": "456", "definition": "Support", "display": "Support"}
    )
    """
    Support

    Support
    """

    four57 = CodeSystemConcept(
        {"code": "457", "definition": "Syringes", "display": "Syringes"}
    )
    """
    Syringes

    Syringes
    """

    four58 = CodeSystemConcept(
        {"code": "458", "definition": "Teeth", "display": "Teeth"}
    )
    """
    Teeth

    Teeth
    """

    four59 = CodeSystemConcept(
        {"code": "459", "definition": "Tenancy Advice", "display": "Tenancy Advice"}
    )
    """
    Tenancy Advice

    Tenancy Advice
    """

    four60 = CodeSystemConcept(
        {"code": "460", "definition": "Terminal Illness", "display": "Terminal Illness"}
    )
    """
    Terminal Illness

    Terminal Illness
    """

    four61 = CodeSystemConcept(
        {"code": "461", "definition": "Therapy", "display": "Therapy"}
    )
    """
    Therapy

    Therapy
    """

    four62 = CodeSystemConcept(
        {"code": "462", "definition": "Transcription", "display": "Transcription"}
    )
    """
    Transcription

    Transcription
    """

    four63 = CodeSystemConcept(
        {
            "code": "463",
            "definition": "Translating Services",
            "display": "Translating Services",
        }
    )
    """
    Translating Services

    Translating Services
    """

    four64 = CodeSystemConcept(
        {"code": "464", "definition": "Translator", "display": "Translator"}
    )
    """
    Translator

    Translator
    """

    four65 = CodeSystemConcept(
        {"code": "465", "definition": "Transport", "display": "Transport"}
    )
    """
    Transport

    Transport
    """

    four66 = CodeSystemConcept(
        {"code": "466", "definition": "Vertebrae", "display": "Vertebrae"}
    )
    """
    Vertebrae

    Vertebrae
    """

    four67 = CodeSystemConcept(
        {"code": "467", "definition": "Violence", "display": "Violence"}
    )
    """
    Violence

    Violence
    """

    four68 = CodeSystemConcept(
        {
            "code": "468",
            "definition": "Vocational Guidance",
            "display": "Vocational Guidance",
        }
    )
    """
    Vocational Guidance

    Vocational Guidance
    """

    four69 = CodeSystemConcept(
        {"code": "469", "definition": "Weight", "display": "Weight"}
    )
    """
    Weight

    Weight
    """

    four70 = CodeSystemConcept(
        {
            "code": "470",
            "definition": "Welfare Assistance",
            "display": "Welfare Assistance",
        }
    )
    """
    Welfare Assistance

    Welfare Assistance
    """

    four71 = CodeSystemConcept(
        {
            "code": "471",
            "definition": "Welfare Counselling",
            "display": "Welfare Counselling",
        }
    )
    """
    Welfare Counselling

    Welfare Counselling
    """

    four72 = CodeSystemConcept(
        {"code": "472", "definition": "Wheelchairs", "display": "Wheelchairs"}
    )
    """
    Wheelchairs

    Wheelchairs
    """

    four73 = CodeSystemConcept(
        {"code": "473", "definition": "Wound Management", "display": "Wound Management"}
    )
    """
    Wound Management

    Wound Management
    """

    four74 = CodeSystemConcept(
        {
            "code": "474",
            "definition": "Young People At Risk",
            "display": "Young People At Risk",
        }
    )
    """
    Young People At Risk

    Young People At Risk
    """

    four75 = CodeSystemConcept(
        {
            "code": "475",
            "definition": "Further Description - Community Health Care",
            "display": "Further Desc. - Community Health Care",
        }
    )
    """
    Further Desc. - Community Health Care

    Further Description - Community Health Care
    """

    four76 = CodeSystemConcept(
        {"code": "476", "definition": "Library", "display": "Library"}
    )
    """
    Library

    Library
    """

    four77 = CodeSystemConcept(
        {"code": "477", "definition": "Community Hours", "display": "Community Hours"}
    )
    """
    Community Hours

    Community Hours
    """

    four78 = CodeSystemConcept(
        {
            "code": "478",
            "definition": "Further Description - Specialist Medical",
            "display": "Further Desc. - Specialist Medical",
        }
    )
    """
    Further Desc. - Specialist Medical

    Further Description - Specialist Medical
    """

    four79 = CodeSystemConcept(
        {"code": "479", "definition": "Hepatology", "display": "Hepatology"}
    )
    """
    Hepatology

    Hepatology
    """

    four80 = CodeSystemConcept(
        {
            "code": "480",
            "definition": "Gastroenterology",
            "display": "Gastroenterology ",
        }
    )
    """
    Gastroenterology 

    Gastroenterology
    """

    four81 = CodeSystemConcept(
        {"code": "481", "definition": "Gynaecology", "display": "Gynaecology"}
    )
    """
    Gynaecology

    Gynaecology
    """

    four82 = CodeSystemConcept(
        {"code": "482", "definition": "Obstetrics", "display": "Obstetrics"}
    )
    """
    Obstetrics

    Obstetrics
    """

    four83 = CodeSystemConcept(
        {
            "code": "483",
            "definition": "Further Description - Specialist Surgical",
            "display": "Further Desc. - Specialist Surgical",
        }
    )
    """
    Further Desc. - Specialist Surgical

    Further Description - Specialist Surgical
    """

    four84 = CodeSystemConcept(
        {
            "code": "484",
            "definition": "Placement Protection",
            "display": "Placement Protection",
        }
    )
    """
    Placement Protection

    Placement Protection
    """

    four85 = CodeSystemConcept(
        {"code": "485", "definition": "Family Violence", "display": "Family Violence"}
    )
    """
    Family Violence

    Family Violence
    """

    four86 = CodeSystemConcept(
        {
            "code": "486",
            "definition": "Integrated Family Services",
            "display": "Integrated Family Services",
        }
    )
    """
    Integrated Family Services

    Integrated Family Services
    """

    four88 = CodeSystemConcept(
        {
            "code": "488",
            "definition": "Diabetes Educator",
            "display": "Diabetes Educator",
        }
    )
    """
    Diabetes Educator

    Diabetes Educator
    """

    four89 = CodeSystemConcept(
        {"code": "489", "definition": "Kinship Care", "display": "Kinship Care"}
    )
    """
    Kinship Care

    Kinship Care
    """

    four90 = CodeSystemConcept(
        {
            "code": "490",
            "definition": "General Mental Health Services",
            "display": "General Mental Health Services",
        }
    )
    """
    General Mental Health Services

    General Mental Health Services
    """

    four91 = CodeSystemConcept(
        {
            "code": "491",
            "definition": "Exercise Physiology",
            "display": "Exercise Physiology",
        }
    )
    """
    Exercise Physiology

    Exercise Physiology
    """

    four92 = CodeSystemConcept(
        {"code": "492", "definition": "Medical Research", "display": "Medical Research"}
    )
    """
    Medical Research

    Medical Research
    """

    four93 = CodeSystemConcept(
        {"code": "493", "definition": "Youth", "display": "Youth"}
    )
    """
    Youth

    Youth
    """

    four94 = CodeSystemConcept(
        {"code": "494", "definition": "Youth Services", "display": "Youth Services"}
    )
    """
    Youth Services

    Youth Services
    """

    four95 = CodeSystemConcept(
        {"code": "495", "definition": "Youth Health", "display": "Youth Health"}
    )
    """
    Youth Health

    Youth Health
    """

    four96 = CodeSystemConcept(
        {
            "code": "496",
            "definition": "Child and Family Services",
            "display": "Child and Family Ser",
        }
    )
    """
    Child and Family Ser

    Child and Family Services
    """

    four97 = CodeSystemConcept(
        {"code": "497", "definition": "Home Visits", "display": "Home Visits"}
    )
    """
    Home Visits

    Home Visits
    """

    four98 = CodeSystemConcept(
        {"code": "498", "definition": "Mobile Services", "display": "Mobile Services"}
    )
    """
    Mobile Services

    Mobile Services
    """

    five00 = CodeSystemConcept(
        {
            "code": "500",
            "definition": "Before and/or After School Care",
            "display": "Before and/or After ",
        }
    )
    """
    Before and/or After 

    Before and/or After School Care
    """

    five01 = CodeSystemConcept(
        {"code": "501", "definition": "Cancer Services", "display": "Cancer Services"}
    )
    """
    Cancer Services

    Cancer Services
    """

    five02 = CodeSystemConcept(
        {
            "code": "502",
            "definition": "Integrated Cancer Services",
            "display": "Integrated Cancer Se",
        }
    )
    """
    Integrated Cancer Se

    Integrated Cancer Services
    """

    five03 = CodeSystemConcept(
        {
            "code": "503",
            "definition": "Multidisciplinary Services",
            "display": "Multidisciplinary Se",
        }
    )
    """
    Multidisciplinary Se

    Multidisciplinary Services
    """

    five04 = CodeSystemConcept(
        {
            "code": "504",
            "definition": "Multidisciplinary Cancer Services",
            "display": "Multidisciplinary Ca",
        }
    )
    """
    Multidisciplinary Ca

    Multidisciplinary Cancer Services
    """

    five05 = CodeSystemConcept(
        {"code": "505", "definition": "Meetings", "display": "Meetings"}
    )
    """
    Meetings

    Meetings
    """

    five06 = CodeSystemConcept(
        {
            "code": "506",
            "definition": "Blood pressure monitoring",
            "display": "Blood pressure monit",
        }
    )
    """
    Blood pressure monit

    Blood pressure monitoring
    """

    five07 = CodeSystemConcept(
        {
            "code": "507",
            "definition": "Dose administration aid",
            "display": "Dose administration ",
        }
    )
    """
    Dose administration 

    Dose administration aid
    """

    five08 = CodeSystemConcept(
        {
            "code": "508",
            "definition": "Medical Equipment Hire",
            "display": "Medical Equipment Hi",
        }
    )
    """
    Medical Equipment Hi

    Medical Equipment Hire
    """

    five09 = CodeSystemConcept(
        {
            "code": "509",
            "definition": "Parenting & family support/education",
            "display": "Parenting/Family Support/Education",
        }
    )
    """
    Parenting/Family Support/Education

    Parenting & family support/education
    """

    five10 = CodeSystemConcept(
        {
            "code": "510",
            "definition": "Deputising Service",
            "display": "Deputising Service",
        }
    )
    """
    Deputising Service

    Deputising Service
    """

    five13 = CodeSystemConcept(
        {
            "code": "513",
            "definition": "Cancer Support Groups",
            "display": "Cancer Support Groups",
        }
    )
    """
    Cancer Support Groups

    Cancer Support Groups
    """

    five14 = CodeSystemConcept(
        {
            "code": "514",
            "definition": "Community Cancer Services",
            "display": "Community Cancer Services",
        }
    )
    """
    Community Cancer Services

    Community Cancer Services
    """

    five30 = CodeSystemConcept(
        {
            "code": "530",
            "definition": "Disability Care Transport",
            "display": "Disability Care Transport",
        }
    )
    """
    Disability Care Transport

    Disability Care Transport
    """

    five31 = CodeSystemConcept(
        {
            "code": "531",
            "definition": "Aged Care Transport",
            "display": "Aged Care Transport",
        }
    )
    """
    Aged Care Transport

    Aged Care Transport
    """

    five32 = CodeSystemConcept(
        {
            "code": "532",
            "definition": "Diabetes Education service",
            "display": "Diabetes Education s",
        }
    )
    """
    Diabetes Education s

    Diabetes Education service
    """

    five33 = CodeSystemConcept(
        {
            "code": "533",
            "definition": "Cardiac Rehabilitation Service ",
            "display": "Cardiac Rehabilitati",
        }
    )
    """
    Cardiac Rehabilitati

    Cardiac Rehabilitation Service 
    """

    five34 = CodeSystemConcept(
        {
            "code": "534",
            "definition": "Young Adult Diabetes services (YADS)",
            "display": "Young Adult Diabetes",
        }
    )
    """
    Young Adult Diabetes

    Young Adult Diabetes services (YADS)
    """

    five35 = CodeSystemConcept(
        {
            "code": "535",
            "definition": "Pulmonary Rehabilitation Service",
            "display": "Pulmonary Rehabilita",
        }
    )
    """
    Pulmonary Rehabilita

    Pulmonary Rehabilitation Service
    """

    five36 = CodeSystemConcept(
        {"code": "536", "definition": "Art therapy", "display": "Art therapy "}
    )
    """
    Art therapy 

    Art therapy
    """

    five37 = CodeSystemConcept(
        {
            "code": "537",
            "definition": "Medication Reviews",
            "display": "Medication Reviews",
        }
    )
    """
    Medication Reviews

    Medication Reviews
    """

    five38 = CodeSystemConcept(
        {
            "code": "538",
            "definition": "Telephone Counselling",
            "display": "Telephone Counselling",
        }
    )
    """
    Telephone Counselling

    Telephone Counselling
    """

    five39 = CodeSystemConcept(
        {
            "code": "539",
            "definition": "Telephone Help Line",
            "display": "Telephone Help Line",
        }
    )
    """
    Telephone Help Line

    Telephone Help Line
    """

    five40 = CodeSystemConcept(
        {"code": "540", "definition": "Online Service", "display": "Online Service"}
    )
    """
    Online Service

    Online Service
    """

    five41 = CodeSystemConcept(
        {
            "code": "541",
            "definition": "Crisis - Mental Health",
            "display": "Crisis - Mental Health",
        }
    )
    """
    Crisis - Mental Health

    Crisis - Mental Health
    """

    five42 = CodeSystemConcept(
        {"code": "542", "definition": "Youth Crisis", "display": "Youth Crisis"}
    )
    """
    Youth Crisis

    Youth Crisis
    """

    five43 = CodeSystemConcept(
        {"code": "543", "definition": "Sexual Assault", "display": "Sexual Assault"}
    )
    """
    Sexual Assault

    Sexual Assault
    """

    five44 = CodeSystemConcept(
        {"code": "544", "definition": "GPAH Other", "display": "GPAH Other"}
    )
    """
    GPAH Other

    GPAH Other
    """

    five45 = CodeSystemConcept(
        {
            "code": "545",
            "definition": "Paediatric Dermatology",
            "display": "Paediatric Dermatology",
        }
    )
    """
    Paediatric Dermatology

    Paediatric Dermatology
    """

    five46 = CodeSystemConcept(
        {
            "code": "546",
            "definition": "Veterans Services",
            "display": "Veterans Services",
        }
    )
    """
    Veterans Services

    Veterans Services
    """

    five47 = CodeSystemConcept(
        {"code": "547", "definition": "Veterans", "display": "Veterans"}
    )
    """
    Veterans

    Veterans
    """

    five48 = CodeSystemConcept(
        {
            "code": "548",
            "definition": "Food Relief/food/meals",
            "display": "Food Relief/Food/Meals",
        }
    )
    """
    Food Relief/Food/Meals

    Food Relief/food/meals
    """

    five50 = CodeSystemConcept(
        {"code": "550", "definition": "Dementia Care", "display": "Dementia Care"}
    )
    """
    Dementia Care

    Dementia Care
    """

    five51 = CodeSystemConcept(
        {"code": "551", "definition": "Alzheimer", "display": "Alzheimer"}
    )
    """
    Alzheimer

    Alzheimer
    """

    five52 = CodeSystemConcept(
        {
            "code": "552",
            "definition": "Drug and/or alcohol support groups",
            "display": "Drug and/or Alcohol Support Groups",
        }
    )
    """
    Drug and/or Alcohol Support Groups

    Drug and/or alcohol support groups
    """

    five53 = CodeSystemConcept(
        {
            "code": "553",
            "definition": "One on One Support/Mentoring/Coaching",
            "display": "1-on-1 Support /Mentoring /Coaching",
        }
    )
    """
    1-on-1 Support /Mentoring /Coaching

    One on One Support/Mentoring/Coaching
    """

    five54 = CodeSystemConcept(
        {
            "code": "554",
            "definition": "Chronic Disease Management",
            "display": "Chronic Disease Management",
        }
    )
    """
    Chronic Disease Management

    Chronic Disease Management
    """

    five55 = CodeSystemConcept(
        {"code": "555", "definition": "Liaison Services", "display": "Liaison Services"}
    )
    """
    Liaison Services

    Liaison Services
    """

    five56 = CodeSystemConcept(
        {
            "code": "556",
            "definition": "Walk in Centre / non emergency",
            "display": "Walk-in Centre /Non-Emergency",
        }
    )
    """
    Walk-in Centre /Non-Emergency

    Walk in Centre / non emergency
    """

    five57 = CodeSystemConcept(
        {"code": "557", "definition": "Inpatients", "display": "Inpatients"}
    )
    """
    Inpatients

    Inpatients
    """

    five58 = CodeSystemConcept(
        {
            "code": "558",
            "definition": "Spiritual Counselling",
            "display": "Spiritual Counselling",
        }
    )
    """
    Spiritual Counselling

    Spiritual Counselling
    """

    five59 = CodeSystemConcept(
        {"code": "559", "definition": "Women's Health", "display": "Women's Health"}
    )
    """
    Women's Health

    Women's Health
    """

    five60 = CodeSystemConcept(
        {"code": "560", "definition": "Men's Health", "display": "Men's Health"}
    )
    """
    Men's Health

    Men's Health
    """

    five61 = CodeSystemConcept(
        {
            "code": "561",
            "definition": "Health education/Health awareness program",
            "display": "Health Education/Awareness Program",
        }
    )
    """
    Health Education/Awareness Program

    Health education/Health awareness program
    """

    five62 = CodeSystemConcept(
        {"code": "562", "definition": "Test Message", "display": "Test Message"}
    )
    """
    Test Message

    Test Message
    """

    five63 = CodeSystemConcept(
        {"code": "563", "definition": "Remedial Massage", "display": "Remedial Massage"}
    )
    """
    Remedial Massage

    Remedial Massage
    """

    five64 = CodeSystemConcept(
        {
            "code": "564",
            "definition": "Adolescent Mental Health Services",
            "display": "Adolescent Mental Health Services",
        }
    )
    """
    Adolescent Mental Health Services

    Adolescent Mental Health Services
    """

    five65 = CodeSystemConcept(
        {
            "code": "565",
            "definition": "Youth drop in/assistance/support",
            "display": "Youth Drop In/Assistance/Support",
        }
    )
    """
    Youth Drop In/Assistance/Support

    Youth drop in/assistance/support
    """

    five66 = CodeSystemConcept(
        {
            "code": "566",
            "definition": "Aboriginal Health Worker",
            "display": "Aboriginal Health Worker",
        }
    )
    """
    Aboriginal Health Worker

    Aboriginal Health Worker
    """

    five67 = CodeSystemConcept(
        {
            "code": "567",
            "definition": "Women's Health Clinic",
            "display": "Women's Health Clinic",
        }
    )
    """
    Women's Health Clinic

    Women's Health Clinic
    """

    five68 = CodeSystemConcept(
        {
            "code": "568",
            "definition": "Men's Health Clinic ",
            "display": "Men's Health Clinic",
        }
    )
    """
    Men's Health Clinic

    Men's Health Clinic 
    """

    five69 = CodeSystemConcept(
        {
            "code": "569",
            "definition": "Migrant Health Clinic",
            "display": "Migrant Health Clinic",
        }
    )
    """
    Migrant Health Clinic

    Migrant Health Clinic
    """

    five70 = CodeSystemConcept(
        {
            "code": "570",
            "definition": "Refugee Health Clinic",
            "display": "Refugee Health Clinic",
        }
    )
    """
    Refugee Health Clinic

    Refugee Health Clinic
    """

    five71 = CodeSystemConcept(
        {
            "code": "571",
            "definition": "Aboriginal Health Clinic",
            "display": "Aboriginal Health Clinic",
        }
    )
    """
    Aboriginal Health Clinic

    Aboriginal Health Clinic
    """

    five72 = CodeSystemConcept(
        {
            "code": "572",
            "definition": "Nurse Practitioner lead Clinic/s",
            "display": "Nurse Practitioner Lead Clinic/s",
        }
    )
    """
    Nurse Practitioner Lead Clinic/s

    Nurse Practitioner lead Clinic/s
    """

    five73 = CodeSystemConcept(
        {
            "code": "573",
            "definition": "Nurse lead Clinic/s",
            "display": "Nurse Lead Clinic/s",
        }
    )
    """
    Nurse Lead Clinic/s

    Nurse lead Clinic/s
    """

    five74 = CodeSystemConcept(
        {
            "code": "574",
            "definition": "Culturally tailored support groups",
            "display": "Culturally Tailored Support Groups",
        }
    )
    """
    Culturally Tailored Support Groups

    Culturally tailored support groups
    """

    five75 = CodeSystemConcept(
        {
            "code": "575",
            "definition": "Culturally tailored health promotion",
            "display": "Culturally Tailored Health Promotion",
        }
    )
    """
    Culturally Tailored Health Promotion

    Culturally tailored health promotion
    """

    five76 = CodeSystemConcept(
        {"code": "576", "definition": "Rehabilitation", "display": "Rehabilitation"}
    )
    """
    Rehabilitation

    Rehabilitation
    """

    five77 = CodeSystemConcept(
        {
            "code": "577",
            "definition": "Education information/referral",
            "display": "Education Information/Referral",
        }
    )
    """
    Education Information/Referral

    Education information/referral
    """

    five80 = CodeSystemConcept(
        {"code": "580", "definition": "Social Work", "display": "Social Work"}
    )
    """
    Social Work

    Social Work
    """

    five81 = CodeSystemConcept(
        {"code": "581", "definition": "Haematology", "display": "Haematology"}
    )
    """
    Haematology

    Haematology
    """

    five82 = CodeSystemConcept(
        {
            "code": "582",
            "definition": "Maternity Shared Care",
            "display": "Maternity Shared Car",
        }
    )
    """
    Maternity Shared Car

    Maternity Shared Care
    """

    five83 = CodeSystemConcept(
        {
            "code": "583",
            "definition": "Rehabilitation Service",
            "display": "Rehabilitation Servi",
        }
    )
    """
    Rehabilitation Servi

    Rehabilitation Service
    """

    five84 = CodeSystemConcept(
        {
            "code": "584",
            "definition": "Cranio-Sacral Therapy",
            "display": "Cranio-sacral Therapy",
        }
    )
    """
    Cranio-sacral Therapy

    Cranio-Sacral Therapy
    """

    five85 = CodeSystemConcept(
        {
            "code": "585",
            "definition": "Prosthetics & Orthotics",
            "display": "Prosthetics & Orthotics",
        }
    )
    """
    Prosthetics & Orthotics

    Prosthetics & Orthotics
    """

    five89 = CodeSystemConcept(
        {
            "code": "589",
            "definition": "Home Medicine Review",
            "display": "Home Medicine Review",
        }
    )
    """
    Home Medicine Review

    Home Medicine Review
    """

    five90 = CodeSystemConcept(
        {"code": "590", "definition": "GPAH - Medical", "display": "GPAH - Medical"}
    )
    """
    GPAH - Medical

    GPAH - Medical
    """

    five91 = CodeSystemConcept(
        {"code": "591", "definition": "Music Therapy", "display": "Music Therapy"}
    )
    """
    Music Therapy

    Music Therapy
    """

    five93 = CodeSystemConcept(
        {"code": "593", "definition": "Falls Prevention", "display": "Falls Prevention"}
    )
    """
    Falls Prevention

    Falls Prevention
    """

    five99 = CodeSystemConcept(
        {
            "code": "599",
            "definition": "Accommodation/Tenancy",
            "display": "Accommodation/Tenancy",
        }
    )
    """
    Accommodation/Tenancy

    Accommodation/Tenancy
    """

    six00 = CodeSystemConcept(
        {
            "code": "600",
            "definition": "Assess-Skill, Ability, Needs",
            "display": "Assess-Skill, Ability, Needs",
        }
    )
    """
    Assess-Skill, Ability, Needs

    Assess-Skill, Ability, Needs
    """

    six01 = CodeSystemConcept(
        {
            "code": "601",
            "definition": "Assist Access/Maintain Employ",
            "display": "Assist Access/Maintain Employ",
        }
    )
    """
    Assist Access/Maintain Employ

    Assist Access/Maintain Employ
    """

    six02 = CodeSystemConcept(
        {
            "code": "602",
            "definition": "Assist Prod-Pers Care/Safety",
            "display": "Assist Prod-Pers Care/Safety",
        }
    )
    """
    Assist Prod-Pers Care/Safety

    Assist Prod-Pers Care/Safety
    """

    six03 = CodeSystemConcept(
        {
            "code": "603",
            "definition": "Assist-Integrate School/Ed",
            "display": "Assist-Integrate School/Ed",
        }
    )
    """
    Assist-Integrate School/Ed

    Assist-Integrate School/Ed
    """

    six04 = CodeSystemConcept(
        {
            "code": "604",
            "definition": "Assist-Life Stage, Transition",
            "display": "Assist-Life Stage, Transition",
        }
    )
    """
    Assist-Life Stage, Transition

    Assist-Life Stage, Transition
    """

    six05 = CodeSystemConcept(
        {
            "code": "605",
            "definition": "Assist-Personal Activities",
            "display": "Assist-Personal Activities",
        }
    )
    """
    Assist-Personal Activities

    Assist-Personal Activities
    """

    six06 = CodeSystemConcept(
        {
            "code": "606",
            "definition": "Assist-Travel/Transport",
            "display": "Assist-Travel/Transport",
        }
    )
    """
    Assist-Travel/Transport

    Assist-Travel/Transport
    """

    six07 = CodeSystemConcept(
        {
            "code": "607",
            "definition": "Assistive Equip-General Tasks",
            "display": "Assistive Equip-General Tasks",
        }
    )
    """
    Assistive Equip-General Tasks

    Assistive Equip-General Tasks
    """

    six08 = CodeSystemConcept(
        {
            "code": "608",
            "definition": "Assistive Equip-Recreation",
            "display": "Assistive Equip-Recreation",
        }
    )
    """
    Assistive Equip-Recreation

    Assistive Equip-Recreation
    """

    six09 = CodeSystemConcept(
        {
            "code": "609",
            "definition": "Assistive Prod-Household Task",
            "display": "Assistive Prod-Household Task",
        }
    )
    """
    Assistive Prod-Household Task

    Assistive Prod-Household Task
    """

    six10 = CodeSystemConcept(
        {"code": "610", "definition": "Behavior Support", "display": "Behavior Support"}
    )
    """
    Behavior Support

    Behavior Support
    """

    six11 = CodeSystemConcept(
        {
            "code": "611",
            "definition": "Comms & Info Equipment",
            "display": "Comms & Info Equipment",
        }
    )
    """
    Comms & Info Equipment

    Comms & Info Equipment
    """

    six12 = CodeSystemConcept(
        {
            "code": "612",
            "definition": "Community Nursing Care",
            "display": "Community Nursing Care",
        }
    )
    """
    Community Nursing Care

    Community Nursing Care
    """

    six13 = CodeSystemConcept(
        {
            "code": "613",
            "definition": "Daily Tasks/Shared Living",
            "display": "Daily Tasks/Shared Living",
        }
    )
    """
    Daily Tasks/Shared Living

    Daily Tasks/Shared Living
    """

    six14 = CodeSystemConcept(
        {
            "code": "614",
            "definition": "Development-Life Skills",
            "display": "Development-Life Skills",
        }
    )
    """
    Development-Life Skills

    Development-Life Skills
    """

    six15 = CodeSystemConcept(
        {
            "code": "615",
            "definition": "Early Childhood Supports",
            "display": "Early Childhood Supports",
        }
    )
    """
    Early Childhood Supports

    Early Childhood Supports
    """

    six16 = CodeSystemConcept(
        {
            "code": "616",
            "definition": "Equipment Special Assess Setup",
            "display": "Equipment Special Assess Setup",
        }
    )
    """
    Equipment Special Assess Setup

    Equipment Special Assess Setup
    """

    six17 = CodeSystemConcept(
        {
            "code": "617",
            "definition": "Hearing Equipment",
            "display": "Hearing Equipment",
        }
    )
    """
    Hearing Equipment

    Hearing Equipment
    """

    six18 = CodeSystemConcept(
        {
            "code": "618",
            "definition": "Home Modification",
            "display": "Home Modification",
        }
    )
    """
    Home Modification

    Home Modification
    """

    six19 = CodeSystemConcept(
        {"code": "619", "definition": "Household Tasks", "display": "Household Tasks"}
    )
    """
    Household Tasks

    Household Tasks
    """

    six20 = CodeSystemConcept(
        {
            "code": "620",
            "definition": "Interpret/Translate",
            "display": "Interpret/Translate",
        }
    )
    """
    Interpret/Translate

    Interpret/Translate
    """

    six21 = CodeSystemConcept(
        {
            "code": "621",
            "definition": "Other Innovative Supports",
            "display": "Other Innovative Supports",
        }
    )
    """
    Other Innovative Supports

    Other Innovative Supports
    """

    six22 = CodeSystemConcept(
        {
            "code": "622",
            "definition": "Participate Community",
            "display": "Participate Community",
        }
    )
    """
    Participate Community

    Participate Community
    """

    six23 = CodeSystemConcept(
        {
            "code": "623",
            "definition": "Personal Mobility Equipment",
            "display": "Personal Mobility Equipment",
        }
    )
    """
    Personal Mobility Equipment

    Personal Mobility Equipment
    """

    six24 = CodeSystemConcept(
        {
            "code": "624",
            "definition": "Physical Wellbeing",
            "display": "Physical Wellbeing",
        }
    )
    """
    Physical Wellbeing

    Physical Wellbeing
    """

    six25 = CodeSystemConcept(
        {"code": "625", "definition": "Plan Management", "display": "Plan Management"}
    )
    """
    Plan Management

    Plan Management
    """

    six26 = CodeSystemConcept(
        {
            "code": "626",
            "definition": "Therapeutic Supports",
            "display": "Therapeutic Supports",
        }
    )
    """
    Therapeutic Supports

    Therapeutic Supports
    """

    six27 = CodeSystemConcept(
        {
            "code": "627",
            "definition": "Training-Travel Independence",
            "display": "Training-Travel Independence",
        }
    )
    """
    Training-Travel Independence

    Training-Travel Independence
    """

    six28 = CodeSystemConcept(
        {
            "code": "628",
            "definition": "Vehicle modifications",
            "display": "Vehicle modifications",
        }
    )
    """
    Vehicle modifications

    Vehicle modifications
    """

    six29 = CodeSystemConcept(
        {"code": "629", "definition": "Vision Equipment", "display": "Vision Equipment"}
    )
    """
    Vision Equipment

    Vision Equipment
    """

    class Meta:
        resource = _resource
