from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ImmunizationRecommendationDateCriterionCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationRecommendationDateCriterionCodes(ValueSet):
    """
    Immunization Recommendation Date Criterion Codes

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support the definition of dates relevant to recommendations
for future doses of vaccines. This value set is provided as a suggestive
example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/immunization-recommendation-date-criterion
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
