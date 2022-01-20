from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.account_status import AccountStatus as AccountStatus_


__all__ = ["AccountStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AccountStatus(AccountStatus_):
    """
    AccountStatus

    Indicates whether the account is available to be used.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/account-status
    """

    class Meta:
        resource = _resource
