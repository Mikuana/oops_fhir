from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.aggregation_mode import (
    AggregationMode as AggregationMode_,
)


__all__ = ["AggregationMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AggregationMode(AggregationMode_):
    """
    AggregationMode

    How resource references can be aggregated.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/resource-aggregation-mode
    """

    class Meta:
        resource = _resource
