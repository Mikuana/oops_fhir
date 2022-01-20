from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.property_representation import (
    PropertyRepresentation as PropertyRepresentation_,
)


__all__ = ["PropertyRepresentation"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class PropertyRepresentation(PropertyRepresentation_):
    """
    PropertyRepresentation

    How a property is represented when serialized.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/property-representation
    """

    class Meta:
        resource = _resource
