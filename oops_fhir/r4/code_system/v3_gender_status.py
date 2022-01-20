from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3GenderStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3GenderStatus:
    """
    v3 Code System GenderStatus

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-GenderStatus
    """

    i = CodeSystemConcept(
        {"code": "I", "definition": "Reproductively intact", "display": "Intact"}
    )
    """
    Intact

    Reproductively intact
    """

    n = CodeSystemConcept(
        {"code": "N", "definition": "Reproductively neutered", "display": "Neutered"}
    )
    """
    Neutered

    Reproductively neutered
    """

    class Meta:
        resource = _resource
