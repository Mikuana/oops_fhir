from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.quantity_comparator import (
    QuantityComparator as QuantityComparator_,
)


__all__ = ["QuantityComparator"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class QuantityComparator(QuantityComparator_):
    """
    QuantityComparator

    How the Quantity should be understood and represented.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/quantity-comparator
    """

    class Meta:
        resource = _resource
