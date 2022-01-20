from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_subtype_codes import (
    ContractSubtypeCodes as ContractSubtypeCodes_,
)


__all__ = ["ContractSubtypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractSubtypeCodes(ContractSubtypeCodes_):
    """
    Contract Subtype Codes

    This value set includes sample Contract Subtype codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-subtype
    """

    class Meta:
        resource = _resource
