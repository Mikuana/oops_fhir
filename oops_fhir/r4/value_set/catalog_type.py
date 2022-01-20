from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.catalog_type import CatalogType as CatalogType_


__all__ = ["CatalogType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CatalogType(CatalogType_):
    """
    CatalogType

    The type of catalog.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/catalogType
    """

    class Meta:
        resource = _resource
