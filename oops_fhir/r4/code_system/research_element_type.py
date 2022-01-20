from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ResearchElementType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ResearchElementType:
    """
    ResearchElementType

    The possible types of research elements (E.g. Population, Exposure,
Outcome).

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/research-element-type
    """

    population = CodeSystemConcept(
        {
            "code": "population",
            "definition": "The element defines the population that forms the basis for research.",
            "display": "Population",
        }
    )
    """
    Population

    The element defines the population that forms the basis for research.
    """

    exposure = CodeSystemConcept(
        {
            "code": "exposure",
            "definition": "The element defines an exposure within the population that is being researched.",
            "display": "Exposure",
        }
    )
    """
    Exposure

    The element defines an exposure within the population that is being researched.
    """

    outcome = CodeSystemConcept(
        {
            "code": "outcome",
            "definition": "The element defines an outcome within the population that is being researched.",
            "display": "Outcome",
        }
    )
    """
    Outcome

    The element defines an outcome within the population that is being researched.
    """

    class Meta:
        resource = _resource
