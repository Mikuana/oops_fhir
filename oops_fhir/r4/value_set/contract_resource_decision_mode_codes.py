from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_resource_decision_mode_codes import (
    ContractResourceDecisionModeCodes as ContractResourceDecisionModeCodes_,
)


__all__ = ["ContractResourceDecisionModeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceDecisionModeCodes(ContractResourceDecisionModeCodes_):
    """
    Contract Resource Decision Mode codes

    This value set contract specific codes for decision modes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-decision-mode
    """

    class Meta:
        resource = _resource
