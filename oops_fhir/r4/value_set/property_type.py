from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.property_type import PropertyType as PropertyType_


__all__ = ["PropertyType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class PropertyType(PropertyType_):
    """
    PropertyType

    The type of a property value.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/concept-property-type
    """

    class Meta:
        resource = _resource
