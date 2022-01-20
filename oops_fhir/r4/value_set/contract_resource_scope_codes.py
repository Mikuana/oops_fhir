from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_resource_scope_codes import (
    ContractResourceScopeCodes as ContractResourceScopeCodes_,
)


__all__ = ["ContractResourceScopeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceScopeCodes(ContractResourceScopeCodes_):
    """
    Contract Resource Scope codes

    This value set contract specific codes for security classification.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-security-classification
    """

    class Meta:
        resource = _resource
