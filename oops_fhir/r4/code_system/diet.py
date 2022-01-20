from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["Diet"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class Diet:
    """
    Diet

    This value set defines a set of codes that can be used to indicate
dietary preferences or restrictions a patient may have.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/diet
    """

    vegetarian = CodeSystemConcept(
        {
            "code": "vegetarian",
            "definition": "Food without meat, poultry or seafood.",
            "display": "Vegetarian",
        }
    )
    """
    Vegetarian

    Food without meat, poultry or seafood.
    """

    dairy_free = CodeSystemConcept(
        {
            "code": "dairy-free",
            "definition": "Excludes dairy products.",
            "display": "Dairy Free",
        }
    )
    """
    Dairy Free

    Excludes dairy products.
    """

    nut_free = CodeSystemConcept(
        {
            "code": "nut-free",
            "definition": "Excludes ingredients containing nuts.",
            "display": "Nut Free",
        }
    )
    """
    Nut Free

    Excludes ingredients containing nuts.
    """

    gluten_free = CodeSystemConcept(
        {
            "code": "gluten-free",
            "definition": "Excludes ingredients containing gluten.",
            "display": "Gluten Free",
        }
    )
    """
    Gluten Free

    Excludes ingredients containing gluten.
    """

    vegan = CodeSystemConcept(
        {
            "code": "vegan",
            "definition": "Food without meat, poultry, seafood, eggs, dairy products and other animal-derived substances.",
            "display": "Vegan",
        }
    )
    """
    Vegan

    Food without meat, poultry, seafood, eggs, dairy products and other animal-derived substances.
    """

    halal = CodeSystemConcept(
        {
            "code": "halal",
            "definition": "Foods that conform to Islamic law.",
            "display": "Halal",
        }
    )
    """
    Halal

    Foods that conform to Islamic law.
    """

    kosher = CodeSystemConcept(
        {
            "code": "kosher",
            "definition": "Foods that conform to Jewish dietary law.",
            "display": "Kosher",
        }
    )
    """
    Kosher

    Foods that conform to Jewish dietary law.
    """

    class Meta:
        resource = _resource
