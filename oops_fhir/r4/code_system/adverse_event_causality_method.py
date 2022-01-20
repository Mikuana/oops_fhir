from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AdverseEventCausalityMethod"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AdverseEventCausalityMethod:
    """
    AdverseEventCausalityMethod

    TODO.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/adverse-event-causality-method
    """

    probability_scale = CodeSystemConcept(
        {"code": "ProbabilityScale", "display": "Probability Scale"}
    )
    """
    Probability Scale

    
    """

    bayesian = CodeSystemConcept({"code": "Bayesian", "display": "Bayesian"})
    """
    Bayesian

    
    """

    checklist = CodeSystemConcept({"code": "Checklist", "display": "Checklist"})
    """
    Checklist

    
    """

    class Meta:
        resource = _resource
