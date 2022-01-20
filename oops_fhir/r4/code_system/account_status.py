from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AccountStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AccountStatus:
    """
    AccountStatus

    Indicates whether the account is available to be used.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/account-status
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "This account is active and may be used.",
            "display": "Active",
        }
    )
    """
    Active

    This account is active and may be used.
    """

    inactive = CodeSystemConcept(
        {
            "code": "inactive",
            "definition": "This account is inactive and should not be used to track financial information.",
            "display": "Inactive",
        }
    )
    """
    Inactive

    This account is inactive and should not be used to track financial information.
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

    on_hold = CodeSystemConcept(
        {
            "code": "on-hold",
            "definition": "This account is on hold.",
            "display": "On Hold",
        }
    )
    """
    On Hold

    This account is on hold.
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": "The account status is unknown.",
            "display": "Unknown",
        }
    )
    """
    Unknown

    The account status is unknown.
    """

    class Meta:
        resource = _resource
