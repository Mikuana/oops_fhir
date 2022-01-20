from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_resource_definition_type_codes import (
    ContractResourceDefinitionTypeCodes as ContractResourceDefinitionTypeCodes_,
)


__all__ = ["ContractResourceDefinitionTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceDefinitionTypeCodes(ContractResourceDefinitionTypeCodes_):
    """
    Contract Resource Definition Type codes

    This value set contract specific codes for status.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-definition-type
    """

    class Meta:
        resource = _resource
