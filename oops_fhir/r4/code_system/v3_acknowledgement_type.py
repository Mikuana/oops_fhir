from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3AcknowledgementType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3AcknowledgementType:
    """
    v3 Code System AcknowledgementType

     This attribute contains an acknowledgement code as described in the HL7
message processing rules.  OpenIssue:  Description was copied from
attribute and needs to be improved to be appropriate for a code system.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-AcknowledgementType
    """

    aa = CodeSystemConcept(
        {
            "code": "AA",
            "definition": "Receiving application successfully processed message.",
            "display": "Application Acknowledgement Accept",
        }
    )
    """
    Application Acknowledgement Accept

    Receiving application successfully processed message.
    """

    ae = CodeSystemConcept(
        {
            "code": "AE",
            "definition": "Receiving application found error in processing message.  Sending error response with additional error detail information.",
            "display": "Application Acknowledgement Error",
        }
    )
    """
    Application Acknowledgement Error

    Receiving application found error in processing message.  Sending error response with additional error detail information.
    """

    ar = CodeSystemConcept(
        {
            "code": "AR",
            "definition": "Receiving application failed to process message for reason unrelated to content or format.  Original message sender must decide on whether to automatically send message again.",
            "display": "Application Acknowledgement Reject",
        }
    )
    """
    Application Acknowledgement Reject

    Receiving application failed to process message for reason unrelated to content or format.  Original message sender must decide on whether to automatically send message again.
    """

    ca = CodeSystemConcept(
        {
            "code": "CA",
            "definition": "Receiving message handling service accepts responsibility for passing message onto receiving application.",
            "display": "Accept Acknowledgement Commit Accept",
        }
    )
    """
    Accept Acknowledgement Commit Accept

    Receiving message handling service accepts responsibility for passing message onto receiving application.
    """

    ce = CodeSystemConcept(
        {
            "code": "CE",
            "definition": "Receiving message handling service cannot accept message for any other reason (e.g. message sequence number, etc.).",
            "display": "Accept Acknowledgement Commit Error",
        }
    )
    """
    Accept Acknowledgement Commit Error

    Receiving message handling service cannot accept message for any other reason (e.g. message sequence number, etc.).
    """

    cr = CodeSystemConcept(
        {
            "code": "CR",
            "definition": "Receiving message handling service rejects message if interaction identifier, version or processing mode is incompatible with known receiving application role information.",
            "display": "Accept Acknowledgement Commit Reject",
        }
    )
    """
    Accept Acknowledgement Commit Reject

    Receiving message handling service rejects message if interaction identifier, version or processing mode is incompatible with known receiving application role information.
    """

    class Meta:
        resource = _resource
