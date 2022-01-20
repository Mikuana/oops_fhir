from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_resource_security_control_codes import (
    ContractResourceSecurityControlCodes as ContractResourceSecurityControlCodes_,
)


__all__ = ["ContractResourceSecurityControlCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceSecurityControlCodes(ContractResourceSecurityControlCodes_):
    """
    Contract Resource Security Control codes

    This value set contract specific codes for security control.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-security-control
    """

    class Meta:
        resource = _resource
