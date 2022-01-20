from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContractResourceAssetTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceAssetTypeCodes:
    """
    Contract Resource Asset Type codes

    This value set contract specific codes for asset type.

    Status: draft - Version: 4.0.1

    Copyright HL7 International.

    http://hl7.org/fhir/contract-asset-type
    """

    participation = CodeSystemConcept(
        {
            "code": "participation",
            "definition": "To be completed",
            "display": "Participation",
        }
    )
    """
    Participation

    To be completed
    """

    class Meta:
        resource = _resource
