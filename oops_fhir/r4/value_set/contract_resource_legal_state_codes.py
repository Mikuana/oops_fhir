from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_resource_legal_state_codes import (
    ContractResourceLegalStateCodes as ContractResourceLegalStateCodes_,
)


__all__ = ["ContractResourceLegalStateCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceLegalStateCodes(ContractResourceLegalStateCodes_):
    """
    Contract Resource Legal State codes

    This value set contract specific codes for status.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-legalstate
    """

    class Meta:
        resource = _resource
