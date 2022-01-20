from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_content_derivation_codes import (
    ContractContentDerivationCodes as ContractContentDerivationCodes_,
)


__all__ = ["ContractContentDerivationCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractContentDerivationCodes(ContractContentDerivationCodes_):
    """
    Contract Content Derivation Codes

    This is an example set of Content Derivative type codes, which represent
the minimal content derived from the basal information source at a
specific stage in its lifecycle, which is sufficient to manage that
source information, for example, in a repository, registry, processes
and workflows, for making access control decisions, and providing query
responses.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-content-derivative
    """

    class Meta:
        resource = _resource
