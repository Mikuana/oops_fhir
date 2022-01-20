from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.discriminator_type import (
    DiscriminatorType as DiscriminatorType_,
)


__all__ = ["DiscriminatorType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DiscriminatorType(DiscriminatorType_):
    """
    DiscriminatorType

    How an element value is interpreted when discrimination is evaluated.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/discriminator-type
    """

    class Meta:
        resource = _resource
