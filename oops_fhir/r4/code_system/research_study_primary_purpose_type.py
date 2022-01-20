from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ResearchStudyPrimaryPurposeType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ResearchStudyPrimaryPurposeType:
    """
    ResearchStudyPrimaryPurposeType

    Codes for the main intent of the study.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/research-study-prim-purp-type
    """

    treatment = CodeSystemConcept(
        {
            "code": "treatment",
            "definition": "One or more interventions are being evaluated for treating a disease, syndrome, or condition.",
            "display": "Treatment",
        }
    )
    """
    Treatment

    One or more interventions are being evaluated for treating a disease, syndrome, or condition.
    """

    prevention = CodeSystemConcept(
        {
            "code": "prevention",
            "definition": "One or more interventions are being assessed for preventing the development of a specific disease or health condition.",
            "display": "Prevention",
        }
    )
    """
    Prevention

    One or more interventions are being assessed for preventing the development of a specific disease or health condition.
    """

    diagnostic = CodeSystemConcept(
        {
            "code": "diagnostic",
            "definition": "One or more interventions are being evaluated for identifying a disease or health condition.",
            "display": "Diagnostic",
        }
    )
    """
    Diagnostic

    One or more interventions are being evaluated for identifying a disease or health condition.
    """

    supportive_care = CodeSystemConcept(
        {
            "code": "supportive-care",
            "definition": "One or more interventions are evaluated for maximizing comfort, minimizing side effects, or mitigating against a decline in the participant's health or function.",
            "display": "Supportive Care",
        }
    )
    """
    Supportive Care

    One or more interventions are evaluated for maximizing comfort, minimizing side effects, or mitigating against a decline in the participant's health or function.
    """

    screening = CodeSystemConcept(
        {
            "code": "screening",
            "definition": "One or more interventions are assessed or examined for identifying a condition, or risk factors for a condition, in people who are not yet known to have the condition or risk factor.",
            "display": "Screening",
        }
    )
    """
    Screening

    One or more interventions are assessed or examined for identifying a condition, or risk factors for a condition, in people who are not yet known to have the condition or risk factor.
    """

    health_services_research = CodeSystemConcept(
        {
            "code": "health-services-research",
            "definition": "One or more interventions for evaluating the delivery, processes, management, organization, or financing of healthcare.",
            "display": "Health Services Research",
        }
    )
    """
    Health Services Research

    One or more interventions for evaluating the delivery, processes, management, organization, or financing of healthcare.
    """

    basic_science = CodeSystemConcept(
        {
            "code": "basic-science",
            "definition": "One or more interventions for examining the basic mechanism of action (for example, physiology or biomechanics of an intervention).",
            "display": "Basic Science",
        }
    )
    """
    Basic Science

    One or more interventions for examining the basic mechanism of action (for example, physiology or biomechanics of an intervention).
    """

    device_feasibility = CodeSystemConcept(
        {
            "code": "device-feasibility",
            "definition": "An intervention of a device product is being evaluated to determine the feasibility of the product or to test a prototype device and not health outcomes. Such studies are conducted to confirm the design and operating specifications of a device before beginning a full clinical trial.",
            "display": "Device Feasibility",
        }
    )
    """
    Device Feasibility

    An intervention of a device product is being evaluated to determine the feasibility of the product or to test a prototype device and not health outcomes. Such studies are conducted to confirm the design and operating specifications of a device before beginning a full clinical trial.
    """

    class Meta:
        resource = _resource
