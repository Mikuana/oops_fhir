from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DiagnosisRole"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DiagnosisRole:
    """
    None

    This value set defines a set of codes that can be used to express the
role of a diagnosis on the Encounter or EpisodeOfCare record.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/diagnosis-role
    """

    ad = CodeSystemConcept({"code": "AD", "display": "Admission diagnosis"})
    """
    Admission diagnosis

    
    """

    dd = CodeSystemConcept({"code": "DD", "display": "Discharge diagnosis"})
    """
    Discharge diagnosis

    
    """

    cc = CodeSystemConcept({"code": "CC", "display": "Chief complaint"})
    """
    Chief complaint

    
    """

    cm = CodeSystemConcept({"code": "CM", "display": "Comorbidity diagnosis"})
    """
    Comorbidity diagnosis

    
    """

    pre_op = CodeSystemConcept({"code": "pre-op", "display": "pre-op diagnosis"})
    """
    pre-op diagnosis

    
    """

    post_op = CodeSystemConcept({"code": "post-op", "display": "post-op diagnosis"})
    """
    post-op diagnosis

    
    """

    billing = CodeSystemConcept({"code": "billing", "display": "Billing"})
    """
    Billing

    
    """

    class Meta:
        resource = _resource
