from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.filter_operator import FilterOperator as FilterOperator_


__all__ = ["FilterOperator"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FilterOperator(FilterOperator_):
    """
    FilterOperator

    The kind of operation to perform as a part of a property based filter.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/filter-operator
    """

    class Meta:
        resource = _resource
