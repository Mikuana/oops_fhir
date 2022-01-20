from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["GuidanceResponseStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class GuidanceResponseStatus:
    """
    GuidanceResponseStatus

    The status of a guidance response.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/guidance-response-status
    """

    success = CodeSystemConcept(
        {
            "code": "success",
            "definition": "The request was processed successfully.",
            "display": "Success",
        }
    )
    """
    Success

    The request was processed successfully.
    """

    data_requested = CodeSystemConcept(
        {
            "code": "data-requested",
            "definition": "The request was processed successfully, but more data may result in a more complete evaluation.",
            "display": "Data Requested",
        }
    )
    """
    Data Requested

    The request was processed successfully, but more data may result in a more complete evaluation.
    """

    data_required = CodeSystemConcept(
        {
            "code": "data-required",
            "definition": "The request was processed, but more data is required to complete the evaluation.",
            "display": "Data Required",
        }
    )
    """
    Data Required

    The request was processed, but more data is required to complete the evaluation.
    """

    in_progress = CodeSystemConcept(
        {
            "code": "in-progress",
            "definition": "The request is currently being processed.",
            "display": "In Progress",
        }
    )
    """
    In Progress

    The request is currently being processed.
    """

    failure = CodeSystemConcept(
        {
            "code": "failure",
            "definition": "The request was not processed successfully.",
            "display": "Failure",
        }
    )
    """
    Failure

    The request was not processed successfully.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The response was entered in error.",
            "display": "Entered In Error",
        }
    )
    """
    Entered In Error

    The response was entered in error.
    """

    class Meta:
        resource = _resource
