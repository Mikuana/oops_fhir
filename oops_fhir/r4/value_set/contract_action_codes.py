from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_action_codes import (
    ContractActionCodes as ContractActionCodes_,
)


__all__ = ["ContractActionCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractActionCodes(ContractActionCodes_):
    """
    Contract Action Codes

    This value set includes sample Contract Action codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-action
    """

    class Meta:
        resource = _resource
