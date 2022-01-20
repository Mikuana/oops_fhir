from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.measure_data_usage import (
    MeasureDataUsage as MeasureDataUsage_,
)


__all__ = ["MeasureDataUsage"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MeasureDataUsage(MeasureDataUsage_):
    """
    MeasureDataUsage

    The intended usage for supplemental data elements in the measure.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/measure-data-usage
    """

    class Meta:
        resource = _resource
