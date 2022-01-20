from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_type_codes import (
    ContractTypeCodes as ContractTypeCodes_,
)


__all__ = ["ContractTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractTypeCodes(ContractTypeCodes_):
    """
    Contract Type Codes

    This value set includes sample Contract Type codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-type
    """

    class Meta:
        resource = _resource
