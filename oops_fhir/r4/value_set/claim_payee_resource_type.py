from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.claim_payee_resource_type import (
    ClaimPayeeResourceType as ClaimPayeeResourceType_,
)


__all__ = ["ClaimPayeeResourceType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ClaimPayeeResourceType(ClaimPayeeResourceType_):
    """
    ClaimPayeeResourceType

    The type of Claim payee Resource.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/ex-payee-resource-type
    """

    class Meta:
        resource = _resource
