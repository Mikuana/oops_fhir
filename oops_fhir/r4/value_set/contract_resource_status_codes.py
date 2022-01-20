from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_resource_status_codes import (
    ContractResourceStatusCodes as ContractResourceStatusCodes_,
)


__all__ = ["ContractResourceStatusCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceStatusCodes(ContractResourceStatusCodes_):
    """
    Contract Resource Status Codes

    This value set contract specific codes for status.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-status
    """

    class Meta:
        resource = _resource
