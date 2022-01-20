from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AnimalSpecies"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AnimalSpecies:
    """
    Animal species

    This example value set defines a set of codes that can be used to
indicate species of animal patients.

    Status: draft - Version: 4.0.1

    Copyright This resource includes content from SNOMED Clinical Terms® (SNOMED CT®) which is copyright of the International Health Terminology Standards Development Organisation (IHTSDO). Implementers of these specifications must have the appropriate SNOMED CT Affiliate license - for more information contact http://www.snomed.org/snomed-ct/get-snomed-ct or info@snomed.org

    http://hl7.org/fhir/animal-species
    """

    canislf = CodeSystemConcept(
        {"code": "canislf", "definition": "Canis lupus familiaris", "display": "Dog"}
    )
    """
    Dog

    Canis lupus familiaris
    """

    ovisa = CodeSystemConcept(
        {"code": "ovisa", "definition": "Ovis aries", "display": "Sheep"}
    )
    """
    Sheep

    Ovis aries
    """

    serinuscd = CodeSystemConcept(
        {
            "code": "serinuscd",
            "definition": "Serinus canaria domestica",
            "display": "Domestic Canary",
        }
    )
    """
    Domestic Canary

    Serinus canaria domestica
    """

    class Meta:
        resource = _resource
