from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["NHINPurposeOfUse"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class NHINPurposeOfUse:
    """
    None

    This value set is suitable for use with the provenance resource. It is
derived from, but not compatible with, the HL7 v3 Purpose of use Code
system.

    Status: active - Version: 2.0

    Copyright None

    http://healthit.gov/nhin/purposeofuse
    """

    treatment = CodeSystemConcept(
        {"code": "TREATMENT", "definition": "Treatment", "display": "Treatment"}
    )
    """
    Treatment

    Treatment
    """

    payment = CodeSystemConcept(
        {"code": "PAYMENT", "definition": "Payment", "display": "Payment"}
    )
    """
    Payment

    Payment
    """

    operations = CodeSystemConcept(
        {
            "code": "OPERATIONS",
            "definition": "Healthcare Operations",
            "display": "Operations",
        }
    )
    """
    Operations

    Healthcare Operations
    """

    sysadmin = CodeSystemConcept(
        {
            "code": "SYSADMIN",
            "definition": "System Administration",
            "display": "Sysadmin",
        }
    )
    """
    Sysadmin

    System Administration
    """

    fraud = CodeSystemConcept(
        {"code": "FRAUD", "definition": "Fraud detection", "display": "Fraud"}
    )
    """
    Fraud

    Fraud detection
    """

    psychotherapy = CodeSystemConcept(
        {
            "code": "PSYCHOTHERAPY",
            "definition": "Use or disclosure of Psychotherapy Notes",
            "display": "Psychotherapy",
        }
    )
    """
    Psychotherapy

    Use or disclosure of Psychotherapy Notes
    """

    training = CodeSystemConcept(
        {
            "code": "TRAINING",
            "definition": "Use or disclosure by the covered entity for its own training programs",
            "display": "Training",
        }
    )
    """
    Training

    Use or disclosure by the covered entity for its own training programs
    """

    legal = CodeSystemConcept(
        {
            "code": "LEGAL",
            "definition": "Use or disclosure by the covered entity to defend itself in a legal action",
            "display": "Legal",
        }
    )
    """
    Legal

    Use or disclosure by the covered entity to defend itself in a legal action
    """

    marketing = CodeSystemConcept(
        {"code": "MARKETING", "definition": "Marketing", "display": "Marketing"}
    )
    """
    Marketing

    Marketing
    """

    directory = CodeSystemConcept(
        {
            "code": "DIRECTORY",
            "definition": "Use and disclosure for facility directories",
            "display": "Directory",
        }
    )
    """
    Directory

    Use and disclosure for facility directories
    """

    family = CodeSystemConcept(
        {
            "code": "FAMILY",
            "definition": "Disclose to a family member, other relative, or a close personal friend of the individual",
            "display": "Family",
        }
    )
    """
    Family

    Disclose to a family member, other relative, or a close personal friend of the individual
    """

    present = CodeSystemConcept(
        {
            "code": "PRESENT",
            "definition": "Uses and disclosures with the individual present.",
            "display": "Present",
        }
    )
    """
    Present

    Uses and disclosures with the individual present.
    """

    emergency = CodeSystemConcept(
        {
            "code": "EMERGENCY",
            "definition": "Permission cannot practicably be provided because of the individual's incapacity or an emergency.",
            "display": "Emergency",
        }
    )
    """
    Emergency

    Permission cannot practicably be provided because of the individual's incapacity or an emergency.
    """

    disaster = CodeSystemConcept(
        {
            "code": "DISASTER",
            "definition": "Use and disclosures for disaster relief purposes.",
            "display": "Disaster",
        }
    )
    """
    Disaster

    Use and disclosures for disaster relief purposes.
    """

    publichealth = CodeSystemConcept(
        {
            "code": "PUBLICHEALTH",
            "definition": "Uses and disclosures for public health activities.",
            "display": "Public Health",
        }
    )
    """
    Public Health

    Uses and disclosures for public health activities.
    """

    abuse = CodeSystemConcept(
        {
            "code": "ABUSE",
            "definition": "Disclosures about victims of abuse, neglect or domestic violence.",
            "display": "Abuse",
        }
    )
    """
    Abuse

    Disclosures about victims of abuse, neglect or domestic violence.
    """

    oversight = CodeSystemConcept(
        {
            "code": "OVERSIGHT",
            "definition": "Uses and disclosures for health oversight activities.",
            "display": "Oversight",
        }
    )
    """
    Oversight

    Uses and disclosures for health oversight activities.
    """

    judicial = CodeSystemConcept(
        {
            "code": "JUDICIAL",
            "definition": "Disclosures for judicial and administrative proceedings.",
            "display": "Judicial",
        }
    )
    """
    Judicial

    Disclosures for judicial and administrative proceedings.
    """

    law = CodeSystemConcept(
        {
            "code": "LAW",
            "definition": "Disclosures for law enforcement purposes.",
            "display": "Law Enforcement",
        }
    )
    """
    Law Enforcement

    Disclosures for law enforcement purposes.
    """

    deceased = CodeSystemConcept(
        {
            "code": "DECEASED",
            "definition": "Uses and disclosures about decedents.",
            "display": "Deceased",
        }
    )
    """
    Deceased

    Uses and disclosures about decedents.
    """

    donation = CodeSystemConcept(
        {
            "code": "DONATION",
            "definition": "Uses and disclosures for cadaveric organ,  eye or tissue donation purposes",
            "display": "Donation",
        }
    )
    """
    Donation

    Uses and disclosures for cadaveric organ,  eye or tissue donation purposes
    """

    research = CodeSystemConcept(
        {
            "code": "RESEARCH",
            "definition": "Uses and disclosures for research purposes.",
            "display": "Research",
        }
    )
    """
    Research

    Uses and disclosures for research purposes.
    """

    threat = CodeSystemConcept(
        {
            "code": "THREAT",
            "definition": "Uses and disclosures to avert a serious threat to health or safety.",
            "display": "Threat",
        }
    )
    """
    Threat

    Uses and disclosures to avert a serious threat to health or safety.
    """

    government = CodeSystemConcept(
        {
            "code": "GOVERNMENT",
            "definition": "Uses and disclosures for specialized government functions.",
            "display": "Government",
        }
    )
    """
    Government

    Uses and disclosures for specialized government functions.
    """

    workerscomp = CodeSystemConcept(
        {
            "code": "WORKERSCOMP",
            "definition": "Disclosures for workers' compensation.",
            "display": "Worker's Comp",
        }
    )
    """
    Worker's Comp

    Disclosures for workers' compensation.
    """

    coverage = CodeSystemConcept(
        {
            "code": "COVERAGE",
            "definition": "Disclosures for insurance or disability coverage determination",
            "display": "Coverage",
        }
    )
    """
    Coverage

    Disclosures for insurance or disability coverage determination
    """

    request = CodeSystemConcept(
        {
            "code": "REQUEST",
            "definition": "Request of the Individual",
            "display": "Request",
        }
    )
    """
    Request

    Request of the Individual
    """

    class Meta:
        resource = _resource
