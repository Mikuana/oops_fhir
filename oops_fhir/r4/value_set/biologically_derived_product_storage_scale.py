from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.biologically_derived_product_storage_scale import (
    BiologicallyDerivedProductStorageScale as BiologicallyDerivedProductStorageScale_,
)


__all__ = ["BiologicallyDerivedProductStorageScale"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class BiologicallyDerivedProductStorageScale(BiologicallyDerivedProductStorageScale_):
    """
    BiologicallyDerivedProductStorageScale

    BiologicallyDerived Product Storage Scale.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/product-storage-scale
    """

    class Meta:
        resource = _resource
