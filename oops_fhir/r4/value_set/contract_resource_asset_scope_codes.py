from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_resource_asset_scope_codes import (
    ContractResourceAssetScopeCodes as ContractResourceAssetScopeCodes_,
)


__all__ = ["ContractResourceAssetScopeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceAssetScopeCodes(ContractResourceAssetScopeCodes_):
    """
    Contract Resource Asset Scope codes

    This value set contract specific codes for asset scope.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-assetscope
    """

    class Meta:
        resource = _resource
