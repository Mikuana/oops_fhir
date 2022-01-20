from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.composite_measure_scoring import (
    CompositeMeasureScoring as CompositeMeasureScoring_,
)


__all__ = ["CompositeMeasureScoring"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CompositeMeasureScoring(CompositeMeasureScoring_):
    """
    CompositeMeasureScoring

    The composite scoring method of the measure.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/composite-measure-scoring
    """

    class Meta:
        resource = _resource
