from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.observation_range_category import (
    ObservationRangeCategory as ObservationRangeCategory_,
)


__all__ = ["ObservationRangeCategory"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ObservationRangeCategory(ObservationRangeCategory_):
    """
    ObservationRangeCategory

    Codes identifying the category of observation range.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/observation-range-category
    """

    class Meta:
        resource = _resource
