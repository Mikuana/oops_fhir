from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.measure_improvement_notation import (
    MeasureImprovementNotation as MeasureImprovementNotation_,
)


__all__ = ["MeasureImprovementNotation"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MeasureImprovementNotation(MeasureImprovementNotation_):
    """
    MeasureImprovementNotation

    Observation values that indicate what change in a measurement value or
score is indicative of an improvement in the measured item or scored
issue.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/measure-improvement-notation
    """

    class Meta:
        resource = _resource
