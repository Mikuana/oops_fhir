from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ConditionVerificationStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ConditionVerificationStatus:
    """
    ConditionVerificationStatus

    The verification status to support or decline the clinical status of the
condition or diagnosis.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/condition-ver-status
    """

    unconfirmed = CodeSystemConcept(
        {
            "code": "unconfirmed",
            "concept": [
                {
                    "code": "provisional",
                    "definition": "This is a tentative diagnosis - still a candidate that is under consideration.",
                    "display": "Provisional",
                },
                {
                    "code": "differential",
                    "definition": "One of a set of potential (and typically mutually exclusive) diagnoses asserted to further guide the diagnostic process and preliminary treatment.",
                    "display": "Differential",
                },
            ],
            "definition": "There is not sufficient diagnostic and/or clinical evidence to treat this as a confirmed condition.",
            "display": "Unconfirmed",
        }
    )
    """
    Unconfirmed

    There is not sufficient diagnostic and/or clinical evidence to treat this as a confirmed condition.
    """

    confirmed = CodeSystemConcept(
        {
            "code": "confirmed",
            "definition": "There is sufficient diagnostic and/or clinical evidence to treat this as a confirmed condition.",
            "display": "Confirmed",
        }
    )
    """
    Confirmed

    There is sufficient diagnostic and/or clinical evidence to treat this as a confirmed condition.
    """

    refuted = CodeSystemConcept(
        {
            "code": "refuted",
            "definition": "This condition has been ruled out by diagnostic and clinical evidence.",
            "display": "Refuted",
        }
    )
    """
    Refuted

    This condition has been ruled out by diagnostic and clinical evidence.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The statement was entered in error and is not valid.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The statement was entered in error and is not valid.
    """

    class Meta:
        resource = _resource
