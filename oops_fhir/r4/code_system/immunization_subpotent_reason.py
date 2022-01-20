from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ImmunizationSubpotentReason"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationSubpotentReason:
    """
    Immunization Subpotent Reason

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the reason why a dose is considered to be
subpotent. This value set is provided as a suggestive example.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/immunization-subpotent-reason
    """

    partial = CodeSystemConcept(
        {
            "code": "partial",
            "definition": "The full volume of the dose was not administered to the patient.",
            "display": "Partial Dose",
        }
    )
    """
    Partial Dose

    The full volume of the dose was not administered to the patient.
    """

    coldchainbreak = CodeSystemConcept(
        {
            "code": "coldchainbreak",
            "definition": "The vaccine experienced a cold chain break.",
            "display": "Cold Chain Break",
        }
    )
    """
    Cold Chain Break

    The vaccine experienced a cold chain break.
    """

    recall = CodeSystemConcept(
        {
            "code": "recall",
            "definition": "The vaccine was recalled by the manufacturer.",
            "display": "Manufacturer Recall",
        }
    )
    """
    Manufacturer Recall

    The vaccine was recalled by the manufacturer.
    """

    class Meta:
        resource = _resource
