from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AdministrativeGender"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AdministrativeGender:
    """
    AdministrativeGender

    The gender of a person used for administrative purposes.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/administrative-gender
    """

    male = CodeSystemConcept(
        {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments",
                    "valueString": "Male",
                }
            ],
            "code": "male",
            "definition": "Male.",
            "display": "Male",
        }
    )
    """
    Male

    Male.
    """

    female = CodeSystemConcept(
        {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments",
                    "valueString": "Female",
                }
            ],
            "code": "female",
            "definition": "Female.",
            "display": "Female",
        }
    )
    """
    Female

    Female.
    """

    other = CodeSystemConcept(
        {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments",
                    "valueString": "The administrative gender is a value other than male/female/unknown. Where this value is selected, systems may often choose to include an extension with the localized more specific value.",
                }
            ],
            "code": "other",
            "definition": "Other.",
            "display": "Other",
        }
    )
    """
    Other

    Other.
    """

    unknown = CodeSystemConcept(
        {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments",
                    "valueString": 'A proper value is applicable, but not known.  Usage Notes: This means the actual value is not known. If the only thing that is unknown is how to properly express the value in the necessary constraints (value set, datatype, etc.), then the OTH or UNC flavor should be used. No properties should be included for a datatype with this property unless:  Those properties themselves directly translate to a semantic of "unknown". (E.g. a local code sent as a translation that conveys \'unknown\') Those properties further qualify the nature of what is unknown. (E.g. specifying a use code of "H" and a URL prefix of "tel:" to convey that it is the home phone number that is unknown.)',
                }
            ],
            "code": "unknown",
            "definition": "Unknown.",
            "display": "Unknown",
        }
    )
    """
    Unknown

    Unknown.
    """

    class Meta:
        resource = _resource
