from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.immunization_program_eligibility import (
    ImmunizationProgramEligibility as ImmunizationProgramEligibility_,
)


__all__ = ["ImmunizationProgramEligibility"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationProgramEligibility(ImmunizationProgramEligibility_):
    """
    Immunization Program Eligibility

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the patient's eligibility for a
vaccination program. This value set is provided as a suggestive example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/immunization-program-eligibility
    """

    class Meta:
        resource = _resource
