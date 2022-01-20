from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContractResourceAssetScopeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceAssetScopeCodes:
    """
    Contract Resource Asset Scope codes

    This value set contract specific codes for asset scope.

    Status: draft - Version: 4.0.1

    Copyright HL7 International.

    http://hl7.org/fhir/contract-asset-scope
    """

    thing = CodeSystemConcept(
        {"code": "thing", "definition": "To be completed", "display": "Thing"}
    )
    """
    Thing

    To be completed
    """

    class Meta:
        resource = _resource
