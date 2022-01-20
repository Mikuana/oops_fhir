from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["medicationKnowledgeCharacteristicCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class medicationKnowledgeCharacteristicCodes:
    """
    Medication knowledge  characteristic  codes

    MedicationKnowledge Characteristic Codes

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/medicationknowledge-characteristic
    """

    imprintcd = CodeSystemConcept(
        {
            "code": "imprintcd",
            "definition": "Identyifying marks on product",
            "display": "Imprint Code",
        }
    )
    """
    Imprint Code

    Identyifying marks on product
    """

    size = CodeSystemConcept(
        {
            "code": "size",
            "definition": "Description of size of the product",
            "display": "Size",
        }
    )
    """
    Size

    Description of size of the product
    """

    shape = CodeSystemConcept(
        {
            "code": "shape",
            "definition": "Description of the shape of the product",
            "display": "Shape",
        }
    )
    """
    Shape

    Description of the shape of the product
    """

    color = CodeSystemConcept(
        {
            "code": "color",
            "definition": "Description of the color of the product",
            "display": "Color",
        }
    )
    """
    Color

    Description of the color of the product
    """

    coating = CodeSystemConcept(
        {
            "code": "coating",
            "definition": "Description of the coating of the product",
            "display": "Coating",
        }
    )
    """
    Coating

    Description of the coating of the product
    """

    scoring = CodeSystemConcept(
        {
            "code": "scoring",
            "definition": "Description of the scoring of the product",
            "display": "Scoring",
        }
    )
    """
    Scoring

    Description of the scoring of the product
    """

    logo = CodeSystemConcept(
        {
            "code": "logo",
            "definition": "Description of the Logo of the product",
            "display": "Logo",
        }
    )
    """
    Logo

    Description of the Logo of the product
    """

    class Meta:
        resource = _resource
