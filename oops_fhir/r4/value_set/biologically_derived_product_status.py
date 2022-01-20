from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.biologically_derived_product_status import (
    BiologicallyDerivedProductStatus as BiologicallyDerivedProductStatus_,
)


__all__ = ["BiologicallyDerivedProductStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class BiologicallyDerivedProductStatus(BiologicallyDerivedProductStatus_):
    """
    BiologicallyDerivedProductStatus

    Biologically Derived Product Status.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/product-status
    """

    class Meta:
        resource = _resource
