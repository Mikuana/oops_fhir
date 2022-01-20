from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.payee_resource_type import (
    PayeeResourceType as PayeeResourceType_,
)


__all__ = ["PayeeResourceType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class PayeeResourceType(PayeeResourceType_):
    """
    PayeeResourceType

    The type of payee Resource.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/resource-type-link
    """

    class Meta:
        resource = _resource
