from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContractResourceAssetAvailiabilityCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceAssetAvailiabilityCodes:
    """
    Contract Resource Asset Availiability codes

    This value set has asset availability codes.

    Status: draft - Version: 4.0.1

    Copyright HL7 International.

    http://hl7.org/fhir/asset-availability
    """

    lease = CodeSystemConcept(
        {"code": "lease", "definition": "To be completed", "display": "Lease"}
    )
    """
    Lease

    To be completed
    """

    class Meta:
        resource = _resource
