from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["EncounterType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class EncounterType:
    """
    Encounter type

    This example value set defines a set of codes that can be used to
indicate the type of encounter: a specific code indicating type of
service provided.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/encounter-type
    """

    adms = CodeSystemConcept(
        {"code": "ADMS", "display": "Annual diabetes mellitus screening"}
    )
    """
    Annual diabetes mellitus screening

    
    """

    bd_bm_clin = CodeSystemConcept(
        {
            "code": "BD/BM-clin",
            "display": "Bone drilling/bone marrow punction in clinic",
        }
    )
    """
    Bone drilling/bone marrow punction in clinic

    
    """

    ccs60 = CodeSystemConcept(
        {"code": "CCS60", "display": "Infant colon screening - 60 minutes"}
    )
    """
    Infant colon screening - 60 minutes

    
    """

    oki = CodeSystemConcept({"code": "OKI", "display": "Outpatient Kenacort injection"})
    """
    Outpatient Kenacort injection

    
    """

    class Meta:
        resource = _resource
