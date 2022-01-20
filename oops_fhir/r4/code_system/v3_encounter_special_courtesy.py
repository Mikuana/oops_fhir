from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3EncounterSpecialCourtesy"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3EncounterSpecialCourtesy:
    """
    v3 Code System EncounterSpecialCourtesy

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-EncounterSpecialCourtesy
    """

    ext = CodeSystemConcept(
        {
            "code": "EXT",
            "definition": "extended courtesy",
            "display": "extended courtesy",
        }
    )
    """
    extended courtesy

    extended courtesy
    """

    nrm = CodeSystemConcept(
        {"code": "NRM", "definition": "normal courtesy", "display": "normal courtesy"}
    )
    """
    normal courtesy

    normal courtesy
    """

    prf = CodeSystemConcept(
        {
            "code": "PRF",
            "definition": "professional courtesy",
            "display": "professional courtesy",
        }
    )
    """
    professional courtesy

    professional courtesy
    """

    stf = CodeSystemConcept(
        {
            "code": "STF",
            "definition": "Courtesies extended to the staff of the entity providing service.",
            "display": "staff",
        }
    )
    """
    staff

    Courtesies extended to the staff of the entity providing service.
    """

    vip = CodeSystemConcept(
        {
            "code": "VIP",
            "definition": "very important person",
            "display": "very important person",
        }
    )
    """
    very important person

    very important person
    """

    class Meta:
        resource = _resource
