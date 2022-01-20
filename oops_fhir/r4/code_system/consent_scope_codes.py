from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ConsentScopeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ConsentScopeCodes:
    """
    Consent Scope Codes

    This value set includes the four Consent scope codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/consentscope
    """

    adr = CodeSystemConcept(
        {
            "code": "adr",
            "definition": "Actions to be taken if they are no longer able to make decisions for themselves",
            "display": "Advanced Care Directive",
        }
    )
    """
    Advanced Care Directive

    Actions to be taken if they are no longer able to make decisions for themselves
    """

    research = CodeSystemConcept(
        {
            "code": "research",
            "definition": "Consent to participate in research protocol and information sharing required",
            "display": "Research",
        }
    )
    """
    Research

    Consent to participate in research protocol and information sharing required
    """

    patient_privacy = CodeSystemConcept(
        {
            "code": "patient-privacy",
            "definition": "Agreement to collect, access, use or disclose (share) information",
            "display": "Privacy Consent",
        }
    )
    """
    Privacy Consent

    Agreement to collect, access, use or disclose (share) information
    """

    treatment = CodeSystemConcept(
        {
            "code": "treatment",
            "definition": "Consent to undergo a specific treatment",
            "display": "Treatment",
        }
    )
    """
    Treatment

    Consent to undergo a specific treatment
    """

    class Meta:
        resource = _resource
