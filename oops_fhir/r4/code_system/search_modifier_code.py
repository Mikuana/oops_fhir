from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SearchModifierCode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SearchModifierCode:
    """
    SearchModifierCode

    A supported modifier for a search parameter.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/search-modifier-code
    """

    missing = CodeSystemConcept(
        {
            "code": "missing",
            "definition": "The search parameter returns resources that have a value or not.",
            "display": "Missing",
        }
    )
    """
    Missing

    The search parameter returns resources that have a value or not.
    """

    exact = CodeSystemConcept(
        {
            "code": "exact",
            "definition": "The search parameter returns resources that have a value that exactly matches the supplied parameter (the whole string, including casing and accents).",
            "display": "Exact",
        }
    )
    """
    Exact

    The search parameter returns resources that have a value that exactly matches the supplied parameter (the whole string, including casing and accents).
    """

    contains = CodeSystemConcept(
        {
            "code": "contains",
            "definition": "The search parameter returns resources that include the supplied parameter value anywhere within the field being searched.",
            "display": "Contains",
        }
    )
    """
    Contains

    The search parameter returns resources that include the supplied parameter value anywhere within the field being searched.
    """

    not_ = CodeSystemConcept(
        {
            "code": "not",
            "definition": "The search parameter returns resources that do not contain a match.",
            "display": "Not",
        }
    )
    """
    Not

    The search parameter returns resources that do not contain a match.
    """

    text = CodeSystemConcept(
        {
            "code": "text",
            "definition": "The search parameter is processed as a string that searches text associated with the code/value - either CodeableConcept.text, Coding.display, or Identifier.type.text.",
            "display": "Text",
        }
    )
    """
    Text

    The search parameter is processed as a string that searches text associated with the code/value - either CodeableConcept.text, Coding.display, or Identifier.type.text.
    """

    in_ = CodeSystemConcept(
        {
            "code": "in",
            "definition": "The search parameter is a URI (relative or absolute) that identifies a value set, and the search parameter tests whether the coding is in the specified value set.",
            "display": "In",
        }
    )
    """
    In

    The search parameter is a URI (relative or absolute) that identifies a value set, and the search parameter tests whether the coding is in the specified value set.
    """

    not_in = CodeSystemConcept(
        {
            "code": "not-in",
            "definition": "The search parameter is a URI (relative or absolute) that identifies a value set, and the search parameter tests whether the coding is not in the specified value set.",
            "display": "Not In",
        }
    )
    """
    Not In

    The search parameter is a URI (relative or absolute) that identifies a value set, and the search parameter tests whether the coding is not in the specified value set.
    """

    below = CodeSystemConcept(
        {
            "code": "below",
            "definition": "The search parameter tests whether the value in a resource is subsumed by the specified value (is-a, or hierarchical relationships).",
            "display": "Below",
        }
    )
    """
    Below

    The search parameter tests whether the value in a resource is subsumed by the specified value (is-a, or hierarchical relationships).
    """

    above = CodeSystemConcept(
        {
            "code": "above",
            "definition": "The search parameter tests whether the value in a resource subsumes the specified value (is-a, or hierarchical relationships).",
            "display": "Above",
        }
    )
    """
    Above

    The search parameter tests whether the value in a resource subsumes the specified value (is-a, or hierarchical relationships).
    """

    type_ = CodeSystemConcept(
        {
            "code": "type",
            "definition": "The search parameter only applies to the Resource Type specified as a modifier (e.g. the modifier is not actually :type, but :Patient etc.).",
            "display": "Type",
        }
    )
    """
    Type

    The search parameter only applies to the Resource Type specified as a modifier (e.g. the modifier is not actually :type, but :Patient etc.).
    """

    identifier = CodeSystemConcept(
        {
            "code": "identifier",
            "definition": "The search parameter applies to the identifier on the resource, not the reference.",
            "display": "Identifier",
        }
    )
    """
    Identifier

    The search parameter applies to the identifier on the resource, not the reference.
    """

    of_type = CodeSystemConcept(
        {
            "code": "ofType",
            "definition": "The search parameter has the format system|code|value, where the system and code refer to an Identifier.type.coding.system and .code, and match if any of the type codes match. All 3 parts must be present.",
            "display": "Of Type",
        }
    )
    """
    Of Type

    The search parameter has the format system|code|value, where the system and code refer to an Identifier.type.coding.system and .code, and match if any of the type codes match. All 3 parts must be present.
    """

    class Meta:
        resource = _resource
