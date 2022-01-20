from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["EnteralFormulaAdditiveTypeCode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class EnteralFormulaAdditiveTypeCode:
    """
    Enteral Formula Additive Type Code

    EnteralFormulaAdditiveType: Codes for the type of modular component such
as protein, carbohydrate or fiber to be provided in addition to or mixed
with the base formula. This value set is provided as a suggestive
example.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/entformula-additive
    """

    lipid = CodeSystemConcept(
        {
            "code": "lipid",
            "definition": "Modular lipid enteral formula component",
            "display": "Lipid",
        }
    )
    """
    Lipid

    Modular lipid enteral formula component
    """

    protein = CodeSystemConcept(
        {
            "code": "protein",
            "definition": "Modular protein enteral formula component",
            "display": "Protein",
        }
    )
    """
    Protein

    Modular protein enteral formula component
    """

    carbohydrate = CodeSystemConcept(
        {
            "code": "carbohydrate",
            "definition": "Modular carbohydrate enteral formula component",
            "display": "Carbohydrate",
        }
    )
    """
    Carbohydrate

    Modular carbohydrate enteral formula component
    """

    fiber = CodeSystemConcept(
        {
            "code": "fiber",
            "definition": "Modular fiber enteral formula component",
            "display": "Fiber",
        }
    )
    """
    Fiber

    Modular fiber enteral formula component
    """

    water = CodeSystemConcept(
        {"code": "water", "definition": "Added water", "display": "Water"}
    )
    """
    Water

    Added water
    """

    class Meta:
        resource = _resource
