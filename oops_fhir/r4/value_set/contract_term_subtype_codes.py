from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_term_subtype_codes import (
    ContractTermSubtypeCodes as ContractTermSubtypeCodes_,
)


__all__ = ["ContractTermSubtypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractTermSubtypeCodes(ContractTermSubtypeCodes_):
    """
    Contract Term Subtype Codes

    This value set includes sample Contract Term SubType codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-term-subtype
    """

    class Meta:
        resource = _resource
