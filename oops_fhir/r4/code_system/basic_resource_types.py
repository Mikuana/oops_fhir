from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["BasicResourceTypes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class BasicResourceTypes:
    """
    Basic Resource Types

    This value set defines codes for resources not yet supported by (or
which will never be supported by) FHIR.  Many of the codes listed here
will eventually be turned into official resources.  However, there is no
guarantee that any particular resource will be created nor that the
scope will be exactly as defined by the codes presented here.  Codes in
this set will be deprecated if/when formal resources are defined that
encompass these concepts.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/basic-resource-type
    """

    consent = CodeSystemConcept(
        {
            "code": "consent",
            "definition": "An assertion of permission for an activity or set of activities to occur, possibly subject to particular limitations; e.g. surgical consent, information disclosure consent, etc.",
            "display": "Consent",
        }
    )
    """
    Consent

    An assertion of permission for an activity or set of activities to occur, possibly subject to particular limitations; e.g. surgical consent, information disclosure consent, etc.
    """

    referral = CodeSystemConcept(
        {
            "code": "referral",
            "definition": "A request that care of a particular type be provided to a patient.  Could involve the transfer of care, a consult, etc.",
            "display": "Referral",
        }
    )
    """
    Referral

    A request that care of a particular type be provided to a patient.  Could involve the transfer of care, a consult, etc.
    """

    advevent = CodeSystemConcept(
        {
            "code": "advevent",
            "definition": "An undesired reaction caused by exposure to some agent (e.g. a medication, immunization, food, or environmental agent).",
            "display": "Adverse Event",
        }
    )
    """
    Adverse Event

    An undesired reaction caused by exposure to some agent (e.g. a medication, immunization, food, or environmental agent).
    """

    aptmtreq = CodeSystemConcept(
        {
            "code": "aptmtreq",
            "definition": "A request that a time be scheduled for a type of service for a specified patient, potentially subject to other constraints",
            "display": "Appointment Request",
        }
    )
    """
    Appointment Request

    A request that a time be scheduled for a type of service for a specified patient, potentially subject to other constraints
    """

    transfer = CodeSystemConcept(
        {
            "code": "transfer",
            "definition": "The transition of a patient or set of material from one location to another",
            "display": "Transfer",
        }
    )
    """
    Transfer

    The transition of a patient or set of material from one location to another
    """

    diet = CodeSystemConcept(
        {
            "code": "diet",
            "definition": "The specification of a set of food and/or other nutritional material to be delivered to a patient.",
            "display": "Diet",
        }
    )
    """
    Diet

    The specification of a set of food and/or other nutritional material to be delivered to a patient.
    """

    adminact = CodeSystemConcept(
        {
            "code": "adminact",
            "definition": "An occurrence of a non-care-related event in the healthcare domain, such as approvals, reviews, etc.",
            "display": "Administrative Activity",
        }
    )
    """
    Administrative Activity

    An occurrence of a non-care-related event in the healthcare domain, such as approvals, reviews, etc.
    """

    exposure = CodeSystemConcept(
        {
            "code": "exposure",
            "definition": "Record of a situation where a subject was exposed to a substance.  Usually of interest to public health.",
            "display": "Exposure",
        }
    )
    """
    Exposure

    Record of a situation where a subject was exposed to a substance.  Usually of interest to public health.
    """

    investigation = CodeSystemConcept(
        {
            "code": "investigation",
            "definition": "A formalized inquiry into the circumstances surrounding a particular unplanned event or potential event for the purposes of identifying possible causes and contributing factors for the event",
            "display": "Investigation",
        }
    )
    """
    Investigation

    A formalized inquiry into the circumstances surrounding a particular unplanned event or potential event for the purposes of identifying possible causes and contributing factors for the event
    """

    account = CodeSystemConcept(
        {
            "code": "account",
            "definition": "A financial instrument used to track costs, charges or other amounts.",
            "display": "Account",
        }
    )
    """
    Account

    A financial instrument used to track costs, charges or other amounts.
    """

    invoice = CodeSystemConcept(
        {
            "code": "invoice",
            "definition": "A request for payment for goods and/or services.  Includes the idea of a healthcare insurance claim.",
            "display": "Invoice",
        }
    )
    """
    Invoice

    A request for payment for goods and/or services.  Includes the idea of a healthcare insurance claim.
    """

    adjudicat = CodeSystemConcept(
        {
            "code": "adjudicat",
            "definition": "The determination of what will be paid against a particular invoice based on coverage, plan rules, etc.",
            "display": "Invoice Adjudication",
        }
    )
    """
    Invoice Adjudication

    The determination of what will be paid against a particular invoice based on coverage, plan rules, etc.
    """

    predetreq = CodeSystemConcept(
        {
            "code": "predetreq",
            "definition": "A request for a pre-determination of the cost that would be paid under an insurance plan for a hypothetical claim for goods or services",
            "display": "Pre-determination Request",
        }
    )
    """
    Pre-determination Request

    A request for a pre-determination of the cost that would be paid under an insurance plan for a hypothetical claim for goods or services
    """

    predetermine = CodeSystemConcept(
        {
            "code": "predetermine",
            "definition": "An adjudication of what would be paid under an insurance plan for a hypothetical claim for goods or services",
            "display": "Predetermination",
        }
    )
    """
    Predetermination

    An adjudication of what would be paid under an insurance plan for a hypothetical claim for goods or services
    """

    study = CodeSystemConcept(
        {
            "code": "study",
            "definition": "An investigation to determine information about a particular therapy or product",
            "display": "Study",
        }
    )
    """
    Study

    An investigation to determine information about a particular therapy or product
    """

    protocol = CodeSystemConcept(
        {
            "code": "protocol",
            "definition": "A set of (possibly conditional) steps to be taken to achieve some aim.  Includes study protocols, treatment protocols, emergency protocols, etc.",
            "display": "Protocol",
        }
    )
    """
    Protocol

    A set of (possibly conditional) steps to be taken to achieve some aim.  Includes study protocols, treatment protocols, emergency protocols, etc.
    """

    class Meta:
        resource = _resource
