from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_data_meaning import (
    ContractDataMeaning as ContractDataMeaning_,
)


__all__ = ["ContractDataMeaning"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractDataMeaning(ContractDataMeaning_):
    """
    ContractDataMeaning

    How a resource reference is interpreted when evaluating contract offers.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-data-meaning
    """

    class Meta:
        resource = _resource
