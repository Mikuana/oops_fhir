from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.compartment_type import (
    CompartmentType as CompartmentType_,
)


__all__ = ["CompartmentType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CompartmentType(CompartmentType_):
    """
    CompartmentType

    Which type a compartment definition describes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/compartment-type
    """

    class Meta:
        resource = _resource
