from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContractResourceExpirationTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceExpirationTypeCodes:
    """
    Contract Resource Expiration Type codes

    This value set contract specific codes for status.

    Status: draft - Version: 4.0.1

    Copyright HL7 International.

    http://hl7.org/fhir/contract-expiration-type
    """

    breach = CodeSystemConcept(
        {"code": "breach", "definition": "To be completed", "display": "Breach"}
    )
    """
    Breach

    To be completed
    """

    class Meta:
        resource = _resource
