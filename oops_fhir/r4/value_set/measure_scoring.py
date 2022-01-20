from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.measure_scoring import MeasureScoring as MeasureScoring_


__all__ = ["MeasureScoring"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MeasureScoring(MeasureScoring_):
    """
    MeasureScoring

    The scoring type of the measure.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/measure-scoring
    """

    class Meta:
        resource = _resource
