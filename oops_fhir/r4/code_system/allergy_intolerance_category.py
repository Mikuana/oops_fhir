from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AllergyIntoleranceCategory"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AllergyIntoleranceCategory:
    """
    AllergyIntoleranceCategory

    Category of an identified substance associated with allergies or
intolerances.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/allergy-intolerance-category
    """

    food = CodeSystemConcept(
        {
            "code": "food",
            "definition": "Any substance consumed to provide nutritional support for the body.",
            "display": "Food",
        }
    )
    """
    Food

    Any substance consumed to provide nutritional support for the body.
    """

    medication = CodeSystemConcept(
        {
            "code": "medication",
            "definition": "Substances administered to achieve a physiological effect.",
            "display": "Medication",
        }
    )
    """
    Medication

    Substances administered to achieve a physiological effect.
    """

    environment = CodeSystemConcept(
        {
            "code": "environment",
            "definition": "Any substances that are encountered in the environment, including any substance not already classified as food, medication, or biologic.",
            "display": "Environment",
        }
    )
    """
    Environment

    Any substances that are encountered in the environment, including any substance not already classified as food, medication, or biologic.
    """

    biologic = CodeSystemConcept(
        {
            "code": "biologic",
            "definition": "A preparation that is synthesized from living organisms or their products, especially a human or animal protein, such as a hormone or antitoxin, that is used as a diagnostic, preventive, or therapeutic agent. Examples of biologic medications include: vaccines; allergenic extracts, which are used for both diagnosis and treatment (for example, allergy shots); gene therapies; cellular therapies.  There are other biologic products, such as tissues, which are not typically associated with allergies.",
            "display": "Biologic",
        }
    )
    """
    Biologic

    A preparation that is synthesized from living organisms or their products, especially a human or animal protein, such as a hormone or antitoxin, that is used as a diagnostic, preventive, or therapeutic agent. Examples of biologic medications include: vaccines; allergenic extracts, which are used for both diagnosis and treatment (for example, allergy shots); gene therapies; cellular therapies.  There are other biologic products, such as tissues, which are not typically associated with allergies.
    """

    class Meta:
        resource = _resource
