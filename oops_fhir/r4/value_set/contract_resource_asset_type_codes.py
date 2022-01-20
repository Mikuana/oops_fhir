from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_resource_asset_type_codes import (
    ContractResourceAssetTypeCodes as ContractResourceAssetTypeCodes_,
)


__all__ = ["ContractResourceAssetTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceAssetTypeCodes(ContractResourceAssetTypeCodes_):
    """
    Contract Resource Asset Type codes

    This value set contract specific codes for asset type.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-assettype
    """

    class Meta:
        resource = _resource
