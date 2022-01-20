from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ConsentState"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ConsentState:
    """
    ConsentState

    Indicates the state of the consent.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/consent-state-codes
    """

    draft = CodeSystemConcept(
        {
            "code": "draft",
            "definition": "The consent is in development or awaiting use but is not yet intended to be acted upon.",
            "display": "Pending",
        }
    )
    """
    Pending

    The consent is in development or awaiting use but is not yet intended to be acted upon.
    """

    proposed = CodeSystemConcept(
        {
            "code": "proposed",
            "definition": "The consent has been proposed but not yet agreed to by all parties. The negotiation stage.",
            "display": "Proposed",
        }
    )
    """
    Proposed

    The consent has been proposed but not yet agreed to by all parties. The negotiation stage.
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "The consent is to be followed and enforced.",
            "display": "Active",
        }
    )
    """
    Active

    The consent is to be followed and enforced.
    """

    rejected = CodeSystemConcept(
        {
            "code": "rejected",
            "definition": "The consent has been rejected by one or more of the parties.",
            "display": "Rejected",
        }
    )
    """
    Rejected

    The consent has been rejected by one or more of the parties.
    """

    inactive = CodeSystemConcept(
        {
            "code": "inactive",
            "definition": "The consent is terminated or replaced.",
            "display": "Inactive",
        }
    )
    """
    Inactive

    The consent is terminated or replaced.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The consent was created wrongly (e.g. wrong patient) and should be ignored.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The consent was created wrongly (e.g. wrong patient) and should be ignored.
    """

    class Meta:
        resource = _resource
