from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MedicationDispenseStatusReasonCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MedicationDispenseStatusReasonCodes:
    """
    Medication dispense  status  reason  codes

    MedicationDispense Status Codes

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/fhir/CodeSystem/medicationdispense-status-reason
    """

    frr01 = CodeSystemConcept(
        {
            "code": "frr01",
            "definition": "The order has been stopped by the prescriber but this fact has not necessarily captured electronically. Example: A verbal stop, a fax, etc.",
            "display": "Order Stopped",
        }
    )
    """
    Order Stopped

    The order has been stopped by the prescriber but this fact has not necessarily captured electronically. Example: A verbal stop, a fax, etc.
    """

    frr02 = CodeSystemConcept(
        {
            "code": "frr02",
            "definition": "Order has not been fulfilled within a reasonable amount of time, and might not be current.",
            "display": "Stale-dated Order",
        }
    )
    """
    Stale-dated Order

    Order has not been fulfilled within a reasonable amount of time, and might not be current.
    """

    frr03 = CodeSystemConcept(
        {
            "code": "frr03",
            "definition": "Data needed to safely act on the order which was expected to become available independent of the order is not yet available. Example: Lab results, diagnostic imaging, etc.",
            "display": "Incomplete data",
        }
    )
    """
    Incomplete data

    Data needed to safely act on the order which was expected to become available independent of the order is not yet available. Example: Lab results, diagnostic imaging, etc.
    """

    frr04 = CodeSystemConcept(
        {
            "code": "frr04",
            "definition": "Product not available or manufactured. Cannot supply.",
            "display": "Product unavailable",
        }
    )
    """
    Product unavailable

    Product not available or manufactured. Cannot supply.
    """

    frr05 = CodeSystemConcept(
        {
            "code": "frr05",
            "definition": "The dispenser has ethical, religious or moral objections to fulfilling the order/dispensing the product.",
            "display": "Ethical/religious",
        }
    )
    """
    Ethical/religious

    The dispenser has ethical, religious or moral objections to fulfilling the order/dispensing the product.
    """

    frr06 = CodeSystemConcept(
        {
            "code": "frr06",
            "definition": "Fulfiller not able to provide appropriate care associated with fulfilling the order. Example: Therapy requires ongoing monitoring by fulfiller and fulfiller will be ending practice, leaving town, unable to schedule necessary time, etc.",
            "display": "Unable to provide care",
        }
    )
    """
    Unable to provide care

    Fulfiller not able to provide appropriate care associated with fulfilling the order. Example: Therapy requires ongoing monitoring by fulfiller and fulfiller will be ending practice, leaving town, unable to schedule necessary time, etc.
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
            "display": "Prescription/Request requires clarification",
        }
    )
    """
    Prescription/Request requires clarification

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
            "display": "Patient is pregnant or breastfeeding",
        }
    )
    """
    Patient is pregnant or breastfeeding

    The patient is pregnant or breast feeding. The therapy will be resumed when the pregnancy is complete and the patient is no longer breastfeeding.
    """

    saig = CodeSystemConcept(
        {
            "code": "saig",
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
            "definition": "Another short-term co-occurring therapy fulfills the same purpose as this therapy. This therapy will be resumed when the co-occuring therapy is complete.",
            "display": "Duplicate therapy",
        }
    )
    """
    Duplicate therapy

    Another short-term co-occurring therapy fulfills the same purpose as this therapy. This therapy will be resumed when the co-occuring therapy is complete.
    """

    sintol = CodeSystemConcept(
        {
            "code": "sintol",
            "definition": "The patient is believed to have an intolerance to a substance that is part of the therapy and the therapy is being temporarily withdrawn to confirm.",
            "display": "Suspected intolerance",
        }
    )
    """
    Suspected intolerance

    The patient is believed to have an intolerance to a substance that is part of the therapy and the therapy is being temporarily withdrawn to confirm.
    """

    surg = CodeSystemConcept(
        {
            "code": "surg",
            "definition": "The drug is contraindicated for patients receiving surgery and the patient is scheduled to be admitted for surgery in the near future. The drug will be resumed when the patient has sufficiently recovered from the surgery.",
            "display": "Patient scheduled for surgery",
        }
    )
    """
    Patient scheduled for surgery

    The drug is contraindicated for patients receiving surgery and the patient is scheduled to be admitted for surgery in the near future. The drug will be resumed when the patient has sufficiently recovered from the surgery.
    """

    washout = CodeSystemConcept(
        {
            "code": "washout",
            "definition": "The patient was previously receiving a medication contraindicated with the current medication. The current medication will remain on hold until the prior medication has been cleansed from their system.",
            "display": "Washout",
        }
    )
    """
    Washout

    The patient was previously receiving a medication contraindicated with the current medication. The current medication will remain on hold until the prior medication has been cleansed from their system.
    """

    outofstock = CodeSystemConcept(
        {
            "code": "outofstock",
            "definition": "Drug out of stock. Cannot supply.",
            "display": "Drug not available - out of stock",
        }
    )
    """
    Drug not available - out of stock

    Drug out of stock. Cannot supply.
    """

    offmarket = CodeSystemConcept(
        {
            "code": "offmarket",
            "definition": "Drug no longer marketed Cannot supply.",
            "display": "Drug not available - off market",
        }
    )
    """
    Drug not available - off market

    Drug no longer marketed Cannot supply.
    """

    class Meta:
        resource = _resource
