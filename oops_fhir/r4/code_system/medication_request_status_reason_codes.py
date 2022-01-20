from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["medicationRequestStatusReasonCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class medicationRequestStatusReasonCodes:
    """
    Medication request  status  reason  codes

    MedicationRequest Status Reason Codes

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/medicationrequest-status-reason
    """

    altchoice = CodeSystemConcept(
        {
            "code": "altchoice",
            "definition": "This therapy has been ordered as a backup to a preferred therapy. This order will be released when and if the preferred therapy is unsuccessful.",
            "display": "Try another treatment first",
        }
    )
    """
    Try another treatment first

    This therapy has been ordered as a backup to a preferred therapy. This order will be released when and if the preferred therapy is unsuccessful.
    """

    clarif = CodeSystemConcept(
        {
            "code": "clarif",
            "definition": "Clarification is required before the order can be acted upon.",
            "display": "Prescription requires clarification",
        }
    )
    """
    Prescription requires clarification

    Clarification is required before the order can be acted upon.
    """

    drughigh = CodeSystemConcept(
        {
            "code": "drughigh",
            "definition": "The current level of the medication in the patient's system is too high. The medication is suspended to allow the level to subside to a safer level.",
            "display": "Drug level too high",
        }
    )
    """
    Drug level too high

    The current level of the medication in the patient's system is too high. The medication is suspended to allow the level to subside to a safer level.
    """

    hospadm = CodeSystemConcept(
        {
            "code": "hospadm",
            "definition": "The patient has been admitted to a care facility and their community medications are suspended until hospital discharge.",
            "display": "Admission to hospital",
        }
    )
    """
    Admission to hospital

    The patient has been admitted to a care facility and their community medications are suspended until hospital discharge.
    """

    labint = CodeSystemConcept(
        {
            "code": "labint",
            "definition": "The therapy would interfere with a planned lab test and the therapy is being withdrawn until the test is completed.",
            "display": "Lab interference issues",
        }
    )
    """
    Lab interference issues

    The therapy would interfere with a planned lab test and the therapy is being withdrawn until the test is completed.
    """

    non_avail = CodeSystemConcept(
        {
            "code": "non-avail",
            "definition": "Patient not available for a period of time due to a scheduled therapy, leave of absence or other reason.",
            "display": "Patient not available",
        }
    )
    """
    Patient not available

    Patient not available for a period of time due to a scheduled therapy, leave of absence or other reason.
    """

    preg = CodeSystemConcept(
        {
            "code": "preg",
            "definition": "The patient is pregnant or breast feeding. The therapy will be resumed when the pregnancy is complete and the patient is no longer breastfeeding.",
            "display": "Parent is pregnant/breast feeding",
        }
    )
    """
    Parent is pregnant/breast feeding

    The patient is pregnant or breast feeding. The therapy will be resumed when the pregnancy is complete and the patient is no longer breastfeeding.
    """

    salg = CodeSystemConcept(
        {
            "code": "salg",
            "definition": "The patient is believed to be allergic to a substance that is part of the therapy and the therapy is being temporarily withdrawn to confirm.",
            "display": "Allergy",
        }
    )
    """
    Allergy

    The patient is believed to be allergic to a substance that is part of the therapy and the therapy is being temporarily withdrawn to confirm.
    """

    sddi = CodeSystemConcept(
        {
            "code": "sddi",
            "definition": "The drug interacts with a short-term treatment that is more urgently required. This order will be resumed when the short-term treatment is complete.",
            "display": "Drug interacts with another drug",
        }
    )
    """
    Drug interacts with another drug

    The drug interacts with a short-term treatment that is more urgently required. This order will be resumed when the short-term treatment is complete.
    """

    sdupther = CodeSystemConcept(
        {
            "code": "sdupther",
            "definition": "The drug interacts with a short-term treatment that is more urgently required. This order will be resumed when the short-term treatment is complete.",
            "display": "Duplicate therapy",
        }
    )
    """
    Duplicate therapy

    The drug interacts with a short-term treatment that is more urgently required. This order will be resumed when the short-term treatment is complete.
    """

    sintol = CodeSystemConcept(
        {
            "code": "sintol",
            "definition": "The drug interacts with a short-term treatment that is more urgently required. This order will be resumed when the short-term treatment is complete.",
            "display": "Suspected intolerance",
        }
    )
    """
    Suspected intolerance

    The drug interacts with a short-term treatment that is more urgently required. This order will be resumed when the short-term treatment is complete.
    """

    surg = CodeSystemConcept(
        {
            "code": "surg",
            "definition": "The drug is contraindicated for patients receiving surgery and the patient is scheduled to be admitted for surgery in the near future. The drug will be resumed when the patient has sufficiently recovered from the surgery.",
            "display": "Patient scheduled for surgery.",
        }
    )
    """
    Patient scheduled for surgery.

    The drug is contraindicated for patients receiving surgery and the patient is scheduled to be admitted for surgery in the near future. The drug will be resumed when the patient has sufficiently recovered from the surgery.
    """

    washout = CodeSystemConcept(
        {
            "code": "washout",
            "definition": "The patient was previously receiving a medication contraindicated with the current medication. The current medication will remain on hold until the prior medication has been cleansed from their system.",
            "display": "Waiting for old drug to wash out",
        }
    )
    """
    Waiting for old drug to wash out

    The patient was previously receiving a medication contraindicated with the current medication. The current medication will remain on hold until the prior medication has been cleansed from their system.
    """

    class Meta:
        resource = _resource
