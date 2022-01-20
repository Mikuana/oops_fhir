from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_resource_asset_context_codes import (
    ContractResourceAssetContextCodes as ContractResourceAssetContextCodes_,
)


__all__ = ["ContractResourceAssetContextCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceAssetContextCodes(ContractResourceAssetContextCodes_):
    """
    Contract Resource Asset Context codes

    This value set contract specific codes for asset context.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-assetcontext
    """

    class Meta:
        resource = _resource
