from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContractResourceAssetContextCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceAssetContextCodes:
    """
    Contract Resource Asset Context codes

    This value set contract specific codes for asset context.

    Status: draft - Version: 4.0.1

    Copyright HL7 International.

    http://hl7.org/fhir/contract-asset-context
    """

    custodian = CodeSystemConcept(
        {"code": "custodian", "definition": "To be completed", "display": "Custodian"}
    )
    """
    Custodian

    To be completed
    """

    class Meta:
        resource = _resource
