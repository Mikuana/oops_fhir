from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_code import v3ActCode


__all__ = ["AccountTypes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AccountTypes(v3ActCode):
    """
    Account Types

    This examples value set defines the set of codes that can be used to
represent the type of an account.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/account-type
    """

    class Meta:
        resource = _resource
