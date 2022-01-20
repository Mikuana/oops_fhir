from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.explanation_of_benefit_status import (
    ExplanationOfBenefitStatus as ExplanationOfBenefitStatus_,
)


__all__ = ["ExplanationOfBenefitStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExplanationOfBenefitStatus(ExplanationOfBenefitStatus_):
    """
    ExplanationOfBenefitStatus

    A code specifying the state of the resource instance.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/explanationofbenefit-status
    """

    class Meta:
        resource = _resource
