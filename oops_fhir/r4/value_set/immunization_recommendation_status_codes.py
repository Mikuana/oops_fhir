from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.immunization_recommendation_status_codes import (
    ImmunizationRecommendationStatusCodes as ImmunizationRecommendationStatusCodes_,
)


__all__ = ["ImmunizationRecommendationStatusCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationRecommendationStatusCodes(ImmunizationRecommendationStatusCodes_):
    """
    Immunization Recommendation Status Codes

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the status of the patient towards
perceived immunity against a vaccine preventable disease. This value set
is provided as a suggestive example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/immunization-recommendation-status
    """

    class Meta:
        resource = _resource
