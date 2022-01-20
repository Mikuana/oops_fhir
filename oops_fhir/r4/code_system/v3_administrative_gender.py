from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3AdministrativeGender"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3AdministrativeGender:
    """
    v3 Code System AdministrativeGender

     The gender of a person used for adminstrative purposes (as opposed to
clinical gender)

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-AdministrativeGender
    """

    f = CodeSystemConcept(
        {
            "code": "F",
            "definition": "Female",
            "designation": [
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Vrouw",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "definition",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Vrouwelijk",
                },
            ],
            "display": "Female",
        }
    )
    """
    Female

    Female
    """

    m = CodeSystemConcept(
        {
            "code": "M",
            "definition": "Male",
            "designation": [
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Man",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "definition",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Man",
                },
            ],
            "display": "Male",
        }
    )
    """
    Male

    Male
    """

    un = CodeSystemConcept(
        {
            "code": "UN",
            "definition": "The gender of a person could not be uniquely defined as male or female, such as hermaphrodite.",
            "designation": [
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Ongedifferentieerd",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "definition",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Het geslacht van een persoon kan niet uniek worden gedefinieerd als man of vrouw, zoals een hermafrodiet.",
                },
            ],
            "display": "Undifferentiated",
        }
    )
    """
    Undifferentiated

    The gender of a person could not be uniquely defined as male or female, such as hermaphrodite.
    """

    class Meta:
        resource = _resource
