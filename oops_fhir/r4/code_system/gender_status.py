from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["GenderStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class GenderStatus:
    """
    Gender status

    This example value set defines a set of codes that can be used to
indicate the current state of the animal's reproductive organs.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/animal-genderstatus
    """

    neutered = CodeSystemConcept(
        {
            "code": "neutered",
            "definition": "The animal has been sterilized, castrated or otherwise made infertile.",
            "designation": [{"language": "nl", "value": "gesteriliseerd"}],
            "display": "Neutered",
        }
    )
    """
    Neutered

    The animal has been sterilized, castrated or otherwise made infertile.
    """

    intact = CodeSystemConcept(
        {
            "code": "intact",
            "definition": "The animal's reproductive organs are intact.",
            "designation": [{"language": "nl", "value": "intact"}],
            "display": "Intact",
        }
    )
    """
    Intact

    The animal's reproductive organs are intact.
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": "Unable to determine whether the animal has been neutered.",
            "designation": [{"language": "nl", "value": "onbekend"}],
            "display": "Unknown",
        }
    )
    """
    Unknown

    Unable to determine whether the animal has been neutered.
    """

    class Meta:
        resource = _resource
