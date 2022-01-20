from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.contract_resource_publication_status_codes import (
    ContractResourcePublicationStatusCodes as ContractResourcePublicationStatusCodes_,
)


__all__ = ["ContractResourcePublicationStatusCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourcePublicationStatusCodes(ContractResourcePublicationStatusCodes_):
    """
    Contract Resource Publication Status codes

    This value set contract specific codes for status.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/contract-publicationstatus
    """

    class Meta:
        resource = _resource
