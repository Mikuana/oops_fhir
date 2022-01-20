from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["EpisodeOfCareType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class EpisodeOfCareType:
    """
    Episode of care type

    This example value set defines a set of codes that can be used to
express the usage type of an EpisodeOfCare record.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/episodeofcare-type
    """

    hacc = CodeSystemConcept({"code": "hacc", "display": "Home and Community Care"})
    """
    Home and Community Care

    
    """

    pac = CodeSystemConcept({"code": "pac", "display": "Post Acute Care"})
    """
    Post Acute Care

    
    """

    diab = CodeSystemConcept(
        {"code": "diab", "display": "Post coordinated diabetes program"}
    )
    """
    Post coordinated diabetes program

    
    """

    da = CodeSystemConcept({"code": "da", "display": "Drug and alcohol rehabilitation"})
    """
    Drug and alcohol rehabilitation

    
    """

    cacp = CodeSystemConcept({"code": "cacp", "display": "Community-based aged care"})
    """
    Community-based aged care

    
    """

    class Meta:
        resource = _resource
