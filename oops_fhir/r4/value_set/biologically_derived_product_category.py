from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.biologically_derived_product_category import (
    BiologicallyDerivedProductCategory as BiologicallyDerivedProductCategory_,
)


__all__ = ["BiologicallyDerivedProductCategory"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class BiologicallyDerivedProductCategory(BiologicallyDerivedProductCategory_):
    """
    BiologicallyDerivedProductCategory

    Biologically Derived Product Category.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/product-category
    """

    class Meta:
        resource = _resource
