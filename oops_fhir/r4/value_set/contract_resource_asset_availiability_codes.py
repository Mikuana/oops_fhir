from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_resource_asset_availiability_codes import (
    ContractResourceAssetAvailiabilityCodes as ContractResourceAssetAvailiabilityCodes_,
)


__all__ = ["ContractResourceAssetAvailiabilityCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceAssetAvailiabilityCodes(ContractResourceAssetAvailiabilityCodes_):
    """
    Contract Resource Asset Availiability codes

    This value set has asset availability codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/asset-availability
    """

    class Meta:
        resource = _resource
