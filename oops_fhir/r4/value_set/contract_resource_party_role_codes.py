from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_resource_party_role_codes import (
    ContractResourcePartyRoleCodes as ContractResourcePartyRoleCodes_,
)


__all__ = ["ContractResourcePartyRoleCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourcePartyRoleCodes(ContractResourcePartyRoleCodes_):
    """
    Contract Resource Party Role codes

    This value set contract specific codes for offer party participation.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-party-role
    """

    class Meta:
        resource = _resource
