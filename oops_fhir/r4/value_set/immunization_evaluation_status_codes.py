from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ImmunizationEvaluationStatusCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationEvaluationStatusCodes(ValueSet):
    """
    Immunization Evaluation Status Codes

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the current status of the evaluation for
vaccine administration event.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/immunization-evaluation-status
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
