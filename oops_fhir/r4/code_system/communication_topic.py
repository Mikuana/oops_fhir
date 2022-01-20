from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CommunicationTopic"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CommunicationTopic:
    """
    CommunicationTopic

    Codes describing the purpose or content of the communication.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/communication-topic
    """

    prescription_refill_request = CodeSystemConcept(
        {
            "code": "prescription-refill-request",
            "definition": "The purpose or content of the communication is a prescription refill request.",
            "display": "Prescription Refill Request",
        }
    )
    """
    Prescription Refill Request

    The purpose or content of the communication is a prescription refill request.
    """

    progress_update = CodeSystemConcept(
        {
            "code": "progress-update",
            "definition": "The purpose or content of the communication is a progress update.",
            "display": "Progress Update",
        }
    )
    """
    Progress Update

    The purpose or content of the communication is a progress update.
    """

    report_labs = CodeSystemConcept(
        {
            "code": "report-labs",
            "definition": "The purpose or content of the communication is to report labs.",
            "display": "Report Labs",
        }
    )
    """
    Report Labs

    The purpose or content of the communication is to report labs.
    """

    appointment_reminder = CodeSystemConcept(
        {
            "code": "appointment-reminder",
            "definition": "The purpose or content of the communication is an appointment reminder.",
            "display": "Appointment Reminder",
        }
    )
    """
    Appointment Reminder

    The purpose or content of the communication is an appointment reminder.
    """

    phone_consult = CodeSystemConcept(
        {
            "code": "phone-consult",
            "definition": "The purpose or content of the communication is a phone consult.",
            "display": "Phone Consult",
        }
    )
    """
    Phone Consult

    The purpose or content of the communication is a phone consult.
    """

    summary_report = CodeSystemConcept(
        {
            "code": "summary-report",
            "definition": "The purpose or content of the communication is a summary report.",
            "display": "Summary Report",
        }
    )
    """
    Summary Report

    The purpose or content of the communication is a summary report.
    """

    class Meta:
        resource = _resource
