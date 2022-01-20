from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ImmunizationEvaluationTargetDiseaseCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationEvaluationTargetDiseaseCodes(ValueSet):
    """
    Immunization Evaluation Target Disease Codes

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the disease that the evaluation is
against. This value set is provided as a suggestive example and includes
the SNOMED CT concepts from the 64572001 (Disease) hierarchy.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/immunization-evaluation-target-disease
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
