from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3EntityRisk"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityRisk:
    """
    v3 Code System EntityRisk

     Kinds of risks associated with the handling of the material..

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-EntityRisk
    """

    agg = CodeSystemConcept(
        {
            "code": "AGG",
            "definition": "A danger that can be associated with certain living subjects, including humans.",
            "display": "aggressive",
        }
    )
    """
    aggressive

    A danger that can be associated with certain living subjects, including humans.
    """

    bio = CodeSystemConcept(
        {
            "code": "BIO",
            "definition": "The dangers associated with normal biological materials. I.e. potential risk of unknown infections.  Routine biological materials from living subjects.",
            "display": "Biological",
        }
    )
    """
    Biological

    The dangers associated with normal biological materials. I.e. potential risk of unknown infections.  Routine biological materials from living subjects.
    """

    cor = CodeSystemConcept(
        {
            "code": "COR",
            "definition": "Material is corrosive and may cause severe injury to skin, mucous membranes and eyes. Avoid any unprotected contact.",
            "display": "Corrosive",
        }
    )
    """
    Corrosive

    Material is corrosive and may cause severe injury to skin, mucous membranes and eyes. Avoid any unprotected contact.
    """

    esc = CodeSystemConcept(
        {
            "code": "ESC",
            "definition": "The entity is at risk for escaping from containment or control.",
            "display": "Escape Risk",
        }
    )
    """
    Escape Risk

    The entity is at risk for escaping from containment or control.
    """

    ifl = CodeSystemConcept(
        {
            "code": "IFL",
            "concept": [
                {
                    "code": "EXP",
                    "definition": "Material is an explosive mixture.  Keep away from fire, sparks, and heat.",
                    "display": "explosive",
                }
            ],
            "definition": "Material is highly inflammable and in certain mixtures (with air) may lead to explosions.  Keep away from fire, sparks and excessive heat.",
            "display": "inflammable",
        }
    )
    """
    inflammable

    Material is highly inflammable and in certain mixtures (with air) may lead to explosions.  Keep away from fire, sparks and excessive heat.
    """

    inf = CodeSystemConcept(
        {
            "code": "INF",
            "concept": [
                {
                    "code": "BHZ",
                    "definition": "Material contains microorganisms that is an environmental hazard.  Must be handled with special care.",
                    "display": "biohazard",
                }
            ],
            "definition": "Material known to be infectious with human pathogenic microorganisms.  Those who handle this material must take precautions for their protection.",
            "display": "infectious",
        }
    )
    """
    infectious

    Material known to be infectious with human pathogenic microorganisms.  Those who handle this material must take precautions for their protection.
    """

    inj = CodeSystemConcept(
        {
            "code": "INJ",
            "definition": "Material is solid and sharp (e.g., cannulas).  Dispose in hard container.",
            "display": "injury hazard",
        }
    )
    """
    injury hazard

    Material is solid and sharp (e.g., cannulas).  Dispose in hard container.
    """

    poi = CodeSystemConcept(
        {
            "code": "POI",
            "definition": "Material is poisonous to humans and/or animals.  Special care must be taken to avoid incorporation, even of small amounts.",
            "display": "poison",
        }
    )
    """
    poison

    Material is poisonous to humans and/or animals.  Special care must be taken to avoid incorporation, even of small amounts.
    """

    rad = CodeSystemConcept(
        {
            "code": "RAD",
            "definition": "Material is a source for ionizing radiation and must be handled with special care to avoid injury of those who handle it and to avoid environmental hazards.",
            "display": "radioactive",
        }
    )
    """
    radioactive

    Material is a source for ionizing radiation and must be handled with special care to avoid injury of those who handle it and to avoid environmental hazards.
    """

    class Meta:
        resource = _resource
