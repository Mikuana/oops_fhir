from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SubstanceCategoryCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SubstanceCategoryCodes:
    """
    Substance Category Codes

    Substance category codes

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/substance-category
    """

    allergen = CodeSystemConcept(
        {
            "code": "allergen",
            "definition": "A substance that causes an allergic reaction.",
            "display": "Allergen",
        }
    )
    """
    Allergen

    A substance that causes an allergic reaction.
    """

    biological = CodeSystemConcept(
        {
            "code": "biological",
            "definition": "A substance that is produced by or extracted from a biological source.",
            "display": "Biological Substance",
        }
    )
    """
    Biological Substance

    A substance that is produced by or extracted from a biological source.
    """

    body = CodeSystemConcept(
        {
            "code": "body",
            "definition": "A substance that comes directly from a human or an animal (e.g. blood, urine, feces, tears, etc.).",
            "display": "Body Substance",
        }
    )
    """
    Body Substance

    A substance that comes directly from a human or an animal (e.g. blood, urine, feces, tears, etc.).
    """

    chemical = CodeSystemConcept(
        {
            "code": "chemical",
            "definition": "Any organic or inorganic substance of a particular molecular identity, including -- (i) any combination of such substances occurring in whole or in part as a result of a chemical reaction or occurring in nature and (ii) any element or uncombined radical (http://www.epa.gov/opptintr/import-export/pubs/importguide.pdf).",
            "display": "Chemical",
        }
    )
    """
    Chemical

    Any organic or inorganic substance of a particular molecular identity, including -- (i) any combination of such substances occurring in whole or in part as a result of a chemical reaction or occurring in nature and (ii) any element or uncombined radical (http://www.epa.gov/opptintr/import-export/pubs/importguide.pdf).
    """

    food = CodeSystemConcept(
        {
            "code": "food",
            "definition": "A food, dietary ingredient, or dietary supplement for human or animal.",
            "display": "Dietary Substance",
        }
    )
    """
    Dietary Substance

    A food, dietary ingredient, or dietary supplement for human or animal.
    """

    drug = CodeSystemConcept(
        {
            "code": "drug",
            "definition": "A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease in man or other animals (Federal Food Drug and Cosmetic Act).",
            "display": "Drug or Medicament",
        }
    )
    """
    Drug or Medicament

    A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease in man or other animals (Federal Food Drug and Cosmetic Act).
    """

    material = CodeSystemConcept(
        {
            "code": "material",
            "definition": "A finished product which is not normally ingested, absorbed or injected (e.g. steel, iron, wood, plastic and paper).",
            "display": "Material",
        }
    )
    """
    Material

    A finished product which is not normally ingested, absorbed or injected (e.g. steel, iron, wood, plastic and paper).
    """

    class Meta:
        resource = _resource
