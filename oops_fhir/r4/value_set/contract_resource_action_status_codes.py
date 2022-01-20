from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_resource_action_status_codes import (
    ContractResourceActionStatusCodes as ContractResourceActionStatusCodes_,
)


__all__ = ["ContractResourceActionStatusCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceActionStatusCodes(ContractResourceActionStatusCodes_):
    """
    Contract Resource Action Status codes

    This value set contract specific codes for action status.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-actionstatus
    """

    class Meta:
        resource = _resource
