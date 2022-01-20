from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ContainerCap"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ContainerCap:
    """
    v3 Code System ContainerCap

     The type of cap associated with a container

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ContainerCap
    """

    underscore_medication_cap = CodeSystemConcept(
        {
            "code": "_MedicationCap",
            "concept": [
                {
                    "code": "CHILD",
                    "definition": "A cap designed to be difficult to open for children.  Generally requires multiple simultaneous actions (e.g. squeeze and twist) to open.  Used for products that may be dangerous if ingested or overdosed by children.",
                    "display": "ChildProof",
                },
                {
                    "code": "EASY",
                    "definition": "A cap designed to be easily removed.  For products intended to be opened by persons with limited strength or dexterity.",
                    "display": "EasyOpen",
                },
            ],
            "definition": "Cap types for medication containers",
            "display": "MedicationCap",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    MedicationCap

    Cap types for medication containers
    """

    film = CodeSystemConcept(
        {
            "code": "FILM",
            "definition": "A non-reactive plastic film covering over the opening of a container.",
            "display": "Film",
        }
    )
    """
    Film

    A non-reactive plastic film covering over the opening of a container.
    """

    foil = CodeSystemConcept(
        {
            "code": "FOIL",
            "definition": "A foil covering (type of foil not specified) over the opening of a container",
            "display": "Foil",
        }
    )
    """
    Foil

    A foil covering (type of foil not specified) over the opening of a container
    """

    push = CodeSystemConcept(
        {
            "code": "PUSH",
            "definition": "A non-threaded cap that forms a tight-fitting closure on a container by pushing the fitted end into the conatiner opening",
            "display": "Push Cap",
        }
    )
    """
    Push Cap

    A non-threaded cap that forms a tight-fitting closure on a container by pushing the fitted end into the conatiner opening
    """

    scr = CodeSystemConcept(
        {
            "code": "SCR",
            "definition": "A threaded cap that is screwed onto the opening of a container",
            "display": "Screw Cap",
        }
    )
    """
    Screw Cap

    A threaded cap that is screwed onto the opening of a container
    """

    class Meta:
        resource = _resource
