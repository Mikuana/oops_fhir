from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.immunization_evaluation_dose_status_codes import (
    ImmunizationEvaluationDoseStatusCodes as ImmunizationEvaluationDoseStatusCodes_,
)


__all__ = ["ImmunizationEvaluationDoseStatusCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationEvaluationDoseStatusCodes(ImmunizationEvaluationDoseStatusCodes_):
    """
    Immunization Evaluation Dose Status codes

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the validity of a dose relative to a
particular recommended schedule. This value set is provided as a
suggestive example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/immunization-evaluation-dose-status
    """

    class Meta:
        resource = _resource
