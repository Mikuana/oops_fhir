from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3EncounterAdmissionSource"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3EncounterAdmissionSource:
    """
    v3 Code System EncounterAdmissionSource

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-EncounterAdmissionSource
    """

    e = CodeSystemConcept(
        {"code": "E", "definition": "emergency", "display": "emergency"}
    )
    """
    emergency

    emergency
    """

    ld = CodeSystemConcept(
        {
            "code": "LD",
            "definition": "labor and delivery",
            "display": "labor and delivery",
        }
    )
    """
    labor and delivery

    labor and delivery
    """

    nb = CodeSystemConcept(
        {"code": "NB", "definition": "newborn", "display": "newborn"}
    )
    """
    newborn

    newborn
    """

    class Meta:
        resource = _resource
