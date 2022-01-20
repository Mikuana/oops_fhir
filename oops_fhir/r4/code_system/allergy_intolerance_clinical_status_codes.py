from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AllergyIntoleranceClinicalStatusCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AllergyIntoleranceClinicalStatusCodes:
    """
    AllergyIntolerance Clinical Status Codes

    Preferred value set for AllergyIntolerance Clinical Status.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "The subject is currently experiencing, or is at risk of, a reaction to the identified substance.",
            "display": "Active",
        }
    )
    """
    Active

    The subject is currently experiencing, or is at risk of, a reaction to the identified substance.
    """

    inactive = CodeSystemConcept(
        {
            "code": "inactive",
            "concept": [
                {
                    "code": "resolved",
                    "definition": "A reaction to the identified substance has been clinically reassessed by testing or re-exposure and is considered no longer to be present. Re-exposure could be accidental, unplanned, or outside of any clinical setting.",
                    "display": "Resolved",
                }
            ],
            "definition": "The subject is no longer at risk of a reaction to the identified substance.",
            "display": "Inactive",
        }
    )
    """
    Inactive

    The subject is no longer at risk of a reaction to the identified substance.
    """

    class Meta:
        resource = _resource
