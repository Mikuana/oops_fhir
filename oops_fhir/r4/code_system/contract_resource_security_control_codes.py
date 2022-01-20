from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContractResourceSecurityControlCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceSecurityControlCodes:
    """
    Contract Resource Security Control codes

    This value set contract specific codes for security control.

    Status: draft - Version: 4.0.1

    Copyright HL7 International.

    http://hl7.org/fhir/contract-security-control
    """

    policy = CodeSystemConcept(
        {"code": "policy", "definition": "To be completed", "display": "Policy"}
    )
    """
    Policy

    To be completed
    """

    class Meta:
        resource = _resource
