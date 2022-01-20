from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContractResourcePartyRoleCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourcePartyRoleCodes:
    """
    Contract Resource Party Role codes

    This value set contract specific codes for offer party participation.

    Status: draft - Version: 4.0.1

    Copyright HL7 International.

    http://hl7.org/fhir/contract-party-role
    """

    flunky = CodeSystemConcept(
        {"code": "flunky", "definition": "To be completed", "display": "FLunky"}
    )
    """
    FLunky

    To be completed
    """

    class Meta:
        resource = _resource
