from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.measure_population_type import (
    MeasurePopulationType as MeasurePopulationType_,
)


__all__ = ["MeasurePopulationType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MeasurePopulationType(MeasurePopulationType_):
    """
    MeasurePopulationType

    The type of population.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/measure-population
    """

    class Meta:
        resource = _resource
