from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ImmunizationProgramEligibility"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationProgramEligibility:
    """
    Immunization Program Eligibility

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the patient's eligibility for a
vaccination program. This value set is provided as a suggestive example.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/immunization-program-eligibility
    """

    ineligible = CodeSystemConcept(
        {
            "code": "ineligible",
            "definition": "The patient is not eligible for the funding program.",
            "display": "Not Eligible",
        }
    )
    """
    Not Eligible

    The patient is not eligible for the funding program.
    """

    uninsured = CodeSystemConcept(
        {
            "code": "uninsured",
            "definition": "The patient is eligible for the funding program because they are uninsured.",
            "display": "Uninsured",
        }
    )
    """
    Uninsured

    The patient is eligible for the funding program because they are uninsured.
    """

    class Meta:
        resource = _resource
