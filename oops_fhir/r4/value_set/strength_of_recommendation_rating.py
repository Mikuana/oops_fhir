from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.strength_of_recommendation_rating import (
    StrengthOfRecommendationRating as StrengthOfRecommendationRating_,
)


__all__ = ["StrengthOfRecommendationRating"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class StrengthOfRecommendationRating(StrengthOfRecommendationRating_):
    """
    StrengthOfRecommendationRating

    A rating system that describes the strength of the recommendation, such
as the GRADE, DynaMed, or HGPS systems.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/recommendation-strength
    """

    class Meta:
        resource = _resource
