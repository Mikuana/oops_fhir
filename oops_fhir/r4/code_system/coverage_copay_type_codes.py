from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CoverageCopayTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CoverageCopayTypeCodes:
    """
    Coverage Copay Type Codes

    This value set includes sample Coverage Copayment Type codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/coverage-copay-type
    """

    gpvisit = CodeSystemConcept(
        {
            "code": "gpvisit",
            "definition": "An office visit for a general practitioner of a discipline.",
            "display": "GP Office Visit",
        }
    )
    """
    GP Office Visit

    An office visit for a general practitioner of a discipline.
    """

    spvisit = CodeSystemConcept(
        {
            "code": "spvisit",
            "definition": "An office visit for a specialist practitioner of a discipline",
            "display": "Specialist Office Visit",
        }
    )
    """
    Specialist Office Visit

    An office visit for a specialist practitioner of a discipline
    """

    emergency = CodeSystemConcept(
        {
            "code": "emergency",
            "definition": "An episode in an emergency department.",
            "display": "Emergency",
        }
    )
    """
    Emergency

    An episode in an emergency department.
    """

    inpthosp = CodeSystemConcept(
        {
            "code": "inpthosp",
            "definition": "An episode of an Inpatient hospital stay.",
            "display": "Inpatient Hospital",
        }
    )
    """
    Inpatient Hospital

    An episode of an Inpatient hospital stay.
    """

    televisit = CodeSystemConcept(
        {
            "code": "televisit",
            "definition": "A visit held where the patient is remote relative to the practitioner, e.g. by phone, computer or video conference.",
            "display": "Tele-visit",
        }
    )
    """
    Tele-visit

    A visit held where the patient is remote relative to the practitioner, e.g. by phone, computer or video conference.
    """

    urgentcare = CodeSystemConcept(
        {
            "code": "urgentcare",
            "definition": "A visit to an urgent care facility - typically a community care clinic.",
            "display": "Urgent Care",
        }
    )
    """
    Urgent Care

    A visit to an urgent care facility - typically a community care clinic.
    """

    copaypct = CodeSystemConcept(
        {
            "code": "copaypct",
            "definition": "A standard percentage applied to all classes or service or product not otherwise specified.",
            "display": "Copay Percentage",
        }
    )
    """
    Copay Percentage

    A standard percentage applied to all classes or service or product not otherwise specified.
    """

    copay = CodeSystemConcept(
        {
            "code": "copay",
            "definition": "A standard fixed currency amount applied to all classes or service or product not otherwise specified.",
            "display": "Copay Amount",
        }
    )
    """
    Copay Amount

    A standard fixed currency amount applied to all classes or service or product not otherwise specified.
    """

    deductible = CodeSystemConcept(
        {
            "code": "deductible",
            "definition": "The accumulated amount of patient payment before the coverage begins to pay for services.",
            "display": "Deductible",
        }
    )
    """
    Deductible

    The accumulated amount of patient payment before the coverage begins to pay for services.
    """

    maxoutofpocket = CodeSystemConcept(
        {
            "code": "maxoutofpocket",
            "definition": "The maximum amout of payment for services which a patient, or family, is expected to incur - typically annually.",
            "display": "Maximum out of pocket",
        }
    )
    """
    Maximum out of pocket

    The maximum amout of payment for services which a patient, or family, is expected to incur - typically annually.
    """

    class Meta:
        resource = _resource
