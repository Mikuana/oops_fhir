from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_resource_expiration_type_codes import (
    ContractResourceExpirationTypeCodes as ContractResourceExpirationTypeCodes_,
)


__all__ = ["ContractResourceExpirationTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceExpirationTypeCodes(ContractResourceExpirationTypeCodes_):
    """
    Contract Resource Expiration Type codes

    This value set contract specific codes for status.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-expiration-type
    """

    class Meta:
        resource = _resource
