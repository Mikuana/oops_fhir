from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["EvidenceVariantState"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class EvidenceVariantState:
    """
    EvidenceVariantState

    Used for results by exposure in variant states such as low-risk, medium-
risk and high-risk states.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/evidence-variant-state
    """

    low_risk = CodeSystemConcept(
        {"code": "low-risk", "definition": "low risk estimate.", "display": "low risk"}
    )
    """
    low risk

    low risk estimate.
    """

    medium_risk = CodeSystemConcept(
        {
            "code": "medium-risk",
            "definition": "medium risk estimate.",
            "display": "medium risk",
        }
    )
    """
    medium risk

    medium risk estimate.
    """

    high_risk = CodeSystemConcept(
        {
            "code": "high-risk",
            "definition": "high risk estimate.",
            "display": "high risk",
        }
    )
    """
    high risk

    high risk estimate.
    """

    class Meta:
        resource = _resource
