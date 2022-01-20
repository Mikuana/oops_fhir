from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_term_type_codes import (
    ContractTermTypeCodes as ContractTermTypeCodes_,
)


__all__ = ["ContractTermTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractTermTypeCodes(ContractTermTypeCodes_):
    """
    Contract Term Type Codes

    This value set includes sample Contract Term Type codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-term-type
    """

    class Meta:
        resource = _resource
