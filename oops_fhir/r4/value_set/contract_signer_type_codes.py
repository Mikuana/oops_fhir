from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_signer_type_codes import (
    ContractSignerTypeCodes as ContractSignerTypeCodes_,
)


__all__ = ["ContractSignerTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractSignerTypeCodes(ContractSignerTypeCodes_):
    """
    Contract Signer Type Codes

    This value set includes sample Contract Signer Type codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-signer-type
    """

    class Meta:
        resource = _resource
