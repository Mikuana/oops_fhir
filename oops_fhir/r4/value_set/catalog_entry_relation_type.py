from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.catalog_entry_relation_type import (
    CatalogEntryRelationType as CatalogEntryRelationType_,
)


__all__ = ["CatalogEntryRelationType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CatalogEntryRelationType(CatalogEntryRelationType_):
    """
    CatalogEntryRelationType

    The type of relations between entries.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/relation-type
    """

    class Meta:
        resource = _resource
