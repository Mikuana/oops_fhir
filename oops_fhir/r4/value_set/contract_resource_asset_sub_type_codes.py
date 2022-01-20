from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_resource_asset_sub_type_codes import (
    ContractResourceAssetSubTypeCodes as ContractResourceAssetSubTypeCodes_,
)


__all__ = ["ContractResourceAssetSubTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceAssetSubTypeCodes(ContractResourceAssetSubTypeCodes_):
    """
    Contract Resource Asset Sub-Type codes

    This value set contract specific codes for asset subtype.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-assetsubtype
    """

    class Meta:
        resource = _resource
