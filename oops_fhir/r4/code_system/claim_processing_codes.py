from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ClaimProcessingCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ClaimProcessingCodes:
    """
    Claim Processing Codes

    This value set includes Claim Processing Outcome codes.

    Status: draft - Version: 4.0.1

    Copyright HL7 Inc.

    http://hl7.org/fhir/remittance-outcome
    """

    queued = CodeSystemConcept(
        {
            "code": "queued",
            "definition": "The Claim/Pre-authorization/Pre-determination has been received but processing has not begun.",
            "display": "Queued",
        }
    )
    """
    Queued

    The Claim/Pre-authorization/Pre-determination has been received but processing has not begun.
    """

    complete = CodeSystemConcept(
        {
            "code": "complete",
            "definition": "The processing has completed without errors",
            "display": "Processing Complete",
        }
    )
    """
    Processing Complete

    The processing has completed without errors
    """

    error = CodeSystemConcept(
        {
            "code": "error",
            "definition": "One or more errors have been detected in the Claim",
            "display": "Error",
        }
    )
    """
    Error

    One or more errors have been detected in the Claim
    """

    partial = CodeSystemConcept(
        {
            "code": "partial",
            "definition": "No errors have been detected in the Claim and some of the adjudication has been performed.",
            "display": "Partial Processing",
        }
    )
    """
    Partial Processing

    No errors have been detected in the Claim and some of the adjudication has been performed.
    """

    class Meta:
        resource = _resource
