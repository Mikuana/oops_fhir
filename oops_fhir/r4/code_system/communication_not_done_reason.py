from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CommunicationNotDoneReason"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CommunicationNotDoneReason:
    """
    CommunicationNotDoneReason

    Codes for the reason why a communication did not happen.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/communication-not-done-reason
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": "The communication was not done due to an unknown reason.",
            "display": "Unknown",
        }
    )
    """
    Unknown

    The communication was not done due to an unknown reason.
    """

    system_error = CodeSystemConcept(
        {
            "code": "system-error",
            "definition": "The communication was not done due to a system error.",
            "display": "System Error",
        }
    )
    """
    System Error

    The communication was not done due to a system error.
    """

    invalid_phone_number = CodeSystemConcept(
        {
            "code": "invalid-phone-number",
            "definition": "The communication was not done due to an invalid phone number.",
            "display": "Invalid Phone Number",
        }
    )
    """
    Invalid Phone Number

    The communication was not done due to an invalid phone number.
    """

    recipient_unavailable = CodeSystemConcept(
        {
            "code": "recipient-unavailable",
            "definition": "The communication was not done due to the recipient being unavailable.",
            "display": "Recipient Unavailable",
        }
    )
    """
    Recipient Unavailable

    The communication was not done due to the recipient being unavailable.
    """

    family_objection = CodeSystemConcept(
        {
            "code": "family-objection",
            "definition": "The communication was not done due to a family objection.",
            "display": "Family Objection",
        }
    )
    """
    Family Objection

    The communication was not done due to a family objection.
    """

    patient_objection = CodeSystemConcept(
        {
            "code": "patient-objection",
            "definition": "The communication was not done due to a patient objection.",
            "display": "Patient Objection",
        }
    )
    """
    Patient Objection

    The communication was not done due to a patient objection.
    """

    class Meta:
        resource = _resource
