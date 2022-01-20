from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ImmunizationRecommendationReasonCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationRecommendationReasonCodes(ValueSet):
    """
    Immunization Recommendation Reason Codes

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the reasons why a given recommendation
status is assigned. This value set is provided as a suggestive example
and includes SNOMED CT concepts.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/immunization-recommendation-reason
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
