from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ObservationStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ObservationStatus:
    """
    ObservationStatus

    Codes providing the status of an observation.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/observation-status
    """

    registered = CodeSystemConcept(
        {
            "code": "registered",
            "definition": "The existence of the observation is registered, but there is no result yet available.",
            "display": "Registered",
        }
    )
    """
    Registered

    The existence of the observation is registered, but there is no result yet available.
    """

    preliminary = CodeSystemConcept(
        {
            "code": "preliminary",
            "definition": "This is an initial or interim observation: data may be incomplete or unverified.",
            "display": "Preliminary",
        }
    )
    """
    Preliminary

    This is an initial or interim observation: data may be incomplete or unverified.
    """

    final = CodeSystemConcept(
        {
            "code": "final",
            "definition": 'The observation is complete and there are no further actions needed. Additional information such "released", "signed", etc would be represented using [Provenance](provenance.html) which provides not only the act but also the actors and dates and other related data. These act states would be associated with an observation status of `preliminary` until they are all completed and then a status of `final` would be applied.',
            "display": "Final",
        }
    )
    """
    Final

    The observation is complete and there are no further actions needed. Additional information such "released", "signed", etc would be represented using [Provenance](provenance.html) which provides not only the act but also the actors and dates and other related data. These act states would be associated with an observation status of `preliminary` until they are all completed and then a status of `final` would be applied.
    """

    amended = CodeSystemConcept(
        {
            "code": "amended",
            "concept": [
                {
                    "code": "corrected",
                    "definition": "Subsequent to being Final, the observation has been modified to correct an error in the test result.",
                    "display": "Corrected",
                }
            ],
            "definition": "Subsequent to being Final, the observation has been modified subsequent.  This includes updates/new information and corrections.",
            "display": "Amended",
        }
    )
    """
    Amended

    Subsequent to being Final, the observation has been modified subsequent.  This includes updates/new information and corrections.
    """

    cancelled = CodeSystemConcept(
        {
            "code": "cancelled",
            "definition": 'The observation is unavailable because the measurement was not started or not completed (also sometimes called "aborted").',
            "display": "Cancelled",
        }
    )
    """
    Cancelled

    The observation is unavailable because the measurement was not started or not completed (also sometimes called "aborted").
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": 'The observation has been withdrawn following previous final release.  This electronic record should never have existed, though it is possible that real-world decisions were based on it. (If real-world activity has occurred, the status should be "cancelled" rather than "entered-in-error".).',
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The observation has been withdrawn following previous final release.  This electronic record should never have existed, though it is possible that real-world decisions were based on it. (If real-world activity has occurred, the status should be "cancelled" rather than "entered-in-error".).
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": 'The authoring/source system does not know which of the status values currently applies for this observation. Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, but the authoring/source system does not know which.',
            "display": "Unknown",
        }
    )
    """
    Unknown

    The authoring/source system does not know which of the status values currently applies for this observation. Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, but the authoring/source system does not know which.
    """

    class Meta:
        resource = _resource
