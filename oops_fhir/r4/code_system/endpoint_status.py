from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["EndpointStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class EndpointStatus:
    """
    EndpointStatus

    The status of the endpoint.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/endpoint-status
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "This endpoint is expected to be active and can be used.",
            "display": "Active",
        }
    )
    """
    Active

    This endpoint is expected to be active and can be used.
    """

    suspended = CodeSystemConcept(
        {
            "code": "suspended",
            "definition": "This endpoint is temporarily unavailable.",
            "display": "Suspended",
        }
    )
    """
    Suspended

    This endpoint is temporarily unavailable.
    """

    error = CodeSystemConcept(
        {
            "code": "error",
            "definition": "This endpoint has exceeded connectivity thresholds and is considered in an error state and should no longer be attempted to connect to until corrective action is taken.",
            "display": "Error",
        }
    )
    """
    Error

    This endpoint has exceeded connectivity thresholds and is considered in an error state and should no longer be attempted to connect to until corrective action is taken.
    """

    off = CodeSystemConcept(
        {
            "code": "off",
            "definition": "This endpoint is no longer to be used.",
            "display": "Off",
        }
    )
    """
    Off

    This endpoint is no longer to be used.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "This instance should not have been part of this patient's medical record.",
            "display": "Entered in error",
        }
    )
    """
    Entered in error

    This instance should not have been part of this patient's medical record.
    """

    test = CodeSystemConcept(
        {
            "code": "test",
            "definition": "This endpoint is not intended for production usage.",
            "display": "Test",
        }
    )
    """
    Test

    This endpoint is not intended for production usage.
    """

    class Meta:
        resource = _resource
