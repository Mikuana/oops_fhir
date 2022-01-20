from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SearchParamType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SearchParamType:
    """
    SearchParamType

    Data types allowed to be used for search parameters.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/search-param-type
    """

    number = CodeSystemConcept(
        {
            "code": "number",
            "definition": "Search parameter SHALL be a number (a whole number, or a decimal).",
            "display": "Number",
        }
    )
    """
    Number

    Search parameter SHALL be a number (a whole number, or a decimal).
    """

    date = CodeSystemConcept(
        {
            "code": "date",
            "definition": "Search parameter is on a date/time. The date format is the standard XML format, though other formats may be supported.",
            "display": "Date/DateTime",
        }
    )
    """
    Date/DateTime

    Search parameter is on a date/time. The date format is the standard XML format, though other formats may be supported.
    """

    string = CodeSystemConcept(
        {
            "code": "string",
            "definition": "Search parameter is a simple string, like a name part. Search is case-insensitive and accent-insensitive. May match just the start of a string. String parameters may contain spaces.",
            "display": "String",
        }
    )
    """
    String

    Search parameter is a simple string, like a name part. Search is case-insensitive and accent-insensitive. May match just the start of a string. String parameters may contain spaces.
    """

    token = CodeSystemConcept(
        {
            "code": "token",
            "definition": 'Search parameter on a coded element or identifier. May be used to search through the text, display, code and code/codesystem (for codes) and label, system and key (for identifier). Its value is either a string or a pair of namespace and value, separated by a "|", depending on the modifier used.',
            "display": "Token",
        }
    )
    """
    Token

    Search parameter on a coded element or identifier. May be used to search through the text, display, code and code/codesystem (for codes) and label, system and key (for identifier). Its value is either a string or a pair of namespace and value, separated by a "|", depending on the modifier used.
    """

    reference = CodeSystemConcept(
        {
            "code": "reference",
            "definition": "A reference to another resource (Reference or canonical).",
            "display": "Reference",
        }
    )
    """
    Reference

    A reference to another resource (Reference or canonical).
    """

    composite = CodeSystemConcept(
        {
            "code": "composite",
            "definition": "A composite search parameter that combines a search on two values together.",
            "display": "Composite",
        }
    )
    """
    Composite

    A composite search parameter that combines a search on two values together.
    """

    quantity = CodeSystemConcept(
        {
            "code": "quantity",
            "definition": "A search parameter that searches on a quantity.",
            "display": "Quantity",
        }
    )
    """
    Quantity

    A search parameter that searches on a quantity.
    """

    uri = CodeSystemConcept(
        {
            "code": "uri",
            "definition": "A search parameter that searches on a URI (RFC 3986).",
            "display": "URI",
        }
    )
    """
    URI

    A search parameter that searches on a URI (RFC 3986).
    """

    special = CodeSystemConcept(
        {
            "code": "special",
            "definition": "Special logic applies to this parameter per the description of the search parameter.",
            "display": "Special",
        }
    )
    """
    Special

    Special logic applies to this parameter per the description of the search parameter.
    """

    class Meta:
        resource = _resource
