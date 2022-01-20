from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["PropertyType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class PropertyType:
    """
    PropertyType

    The type of a property value.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/concept-property-type
    """

    code = CodeSystemConcept(
        {
            "code": "code",
            "definition": "The property value is a code that identifies a concept defined in the code system.",
            "display": "code (internal reference)",
        }
    )
    """
    code (internal reference)

    The property value is a code that identifies a concept defined in the code system.
    """

    coding = CodeSystemConcept(
        {
            "code": "Coding",
            "definition": "The property  value is a code defined in an external code system. This may be used for translations, but is not the intent.",
            "display": "Coding (external reference)",
        }
    )
    """
    Coding (external reference)

    The property  value is a code defined in an external code system. This may be used for translations, but is not the intent.
    """

    string = CodeSystemConcept(
        {
            "code": "string",
            "definition": "The property value is a string.",
            "display": "string",
        }
    )
    """
    string

    The property value is a string.
    """

    integer = CodeSystemConcept(
        {
            "code": "integer",
            "definition": "The property value is a string (often used to assign ranking values to concepts for supporting score assessments).",
            "display": "integer",
        }
    )
    """
    integer

    The property value is a string (often used to assign ranking values to concepts for supporting score assessments).
    """

    boolean = CodeSystemConcept(
        {
            "code": "boolean",
            "definition": "The property value is a boolean true | false.",
            "display": "boolean",
        }
    )
    """
    boolean

    The property value is a boolean true | false.
    """

    date_time = CodeSystemConcept(
        {
            "code": "dateTime",
            "definition": "The property is a date or a date + time.",
            "display": "dateTime",
        }
    )
    """
    dateTime

    The property is a date or a date + time.
    """

    decimal = CodeSystemConcept(
        {
            "code": "decimal",
            "definition": "The property value is a decimal number.",
            "display": "decimal",
        }
    )
    """
    decimal

    The property value is a decimal number.
    """

    class Meta:
        resource = _resource
