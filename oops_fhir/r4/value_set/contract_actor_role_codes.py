from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_actor_role_codes import (
    ContractActorRoleCodes as ContractActorRoleCodes_,
)


__all__ = ["ContractActorRoleCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractActorRoleCodes(ContractActorRoleCodes_):
    """
    Contract Actor Role Codes

    This value set includes sample Contract Actor Role codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-actorrole
    """

    class Meta:
        resource = _resource
