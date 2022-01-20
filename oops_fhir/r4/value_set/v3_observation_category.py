from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_observation_category import (
    v3ObservationCategory as v3ObservationCategory_,
)


__all__ = ["v3ObservationCategory"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ObservationCategory(v3ObservationCategory_):
    """
    v3 Code System ObservationCategory

     High level observation categories for the general type of observation
being made. URL: http://hl7-fhir.github.io/valueset-observation-
category.html This is an inline code system
http://hl7.org/fhir/observation-category.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ObservationCategory
    """

    class Meta:
        resource = _resource
