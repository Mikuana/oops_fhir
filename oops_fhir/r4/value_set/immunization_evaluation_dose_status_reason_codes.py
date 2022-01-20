from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.immunization_evaluation_dose_status_reason_codes import (
    ImmunizationEvaluationDoseStatusReasonCodes as ImmunizationEvaluationDoseStatusReasonCodes_,
)


__all__ = ["ImmunizationEvaluationDoseStatusReasonCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationEvaluationDoseStatusReasonCodes(
    ImmunizationEvaluationDoseStatusReasonCodes_
):
    """
    Immunization Evaluation Dose Status Reason codes

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the reason why an administered dose has
been assigned a particular status. Often, this reason describes why a
dose is considered invalid. This value set is provided as a suggestive
example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/immunization-evaluation-dose-status-reason
    """

    class Meta:
        resource = _resource
