from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["InsurancePlanType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class InsurancePlanType:
    """
    Insurance plan type

    This example value set defines a set of codes that can be used to
indicate a type of insurance plan.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/insurance-plan-type
    """

    medical = CodeSystemConcept({"code": "medical", "display": "Medical"})
    """
    Medical

    
    """

    dental = CodeSystemConcept({"code": "dental", "display": "Dental"})
    """
    Dental

    
    """

    mental = CodeSystemConcept({"code": "mental", "display": "Mental Health"})
    """
    Mental Health

    
    """

    subst_ab = CodeSystemConcept({"code": "subst-ab", "display": "Substance Abuse"})
    """
    Substance Abuse

    
    """

    vision = CodeSystemConcept({"code": "vision", "display": "Vision"})
    """
    Vision

    
    """

    drug = CodeSystemConcept({"code": "Drug", "display": "Drug"})
    """
    Drug

    
    """

    short_term = CodeSystemConcept({"code": "short-term", "display": "Short Term"})
    """
    Short Term

    
    """

    long_term = CodeSystemConcept({"code": "long-term", "display": "Long Term Care"})
    """
    Long Term Care

    
    """

    hospice = CodeSystemConcept({"code": "hospice", "display": "Hospice"})
    """
    Hospice

    
    """

    home = CodeSystemConcept({"code": "home", "display": "Home Health"})
    """
    Home Health

    
    """

    class Meta:
        resource = _resource
