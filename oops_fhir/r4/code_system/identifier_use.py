from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["IdentifierUse"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class IdentifierUse:
    """
    IdentifierUse

    Identifies the purpose for this identifier, if known .

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/identifier-use
    """

    usual = CodeSystemConcept(
        {
            "code": "usual",
            "definition": "The identifier recommended for display and use in real-world interactions.",
            "display": "Usual",
        }
    )
    """
    Usual

    The identifier recommended for display and use in real-world interactions.
    """

    official = CodeSystemConcept(
        {
            "code": "official",
            "definition": 'The identifier considered to be most trusted for the identification of this item. Sometimes also known as "primary" and "main". The determination of "official" is subjective and implementation guides often provide additional guidelines for use.',
            "display": "Official",
        }
    )
    """
    Official

    The identifier considered to be most trusted for the identification of this item. Sometimes also known as "primary" and "main". The determination of "official" is subjective and implementation guides often provide additional guidelines for use.
    """

    temp = CodeSystemConcept(
        {"code": "temp", "definition": "A temporary identifier.", "display": "Temp"}
    )
    """
    Temp

    A temporary identifier.
    """

    secondary = CodeSystemConcept(
        {
            "code": "secondary",
            "definition": "An identifier that was assigned in secondary use - it serves to identify the object in a relative context, but cannot be consistently assigned to the same object again in a different context.",
            "display": "Secondary",
        }
    )
    """
    Secondary

    An identifier that was assigned in secondary use - it serves to identify the object in a relative context, but cannot be consistently assigned to the same object again in a different context.
    """

    old = CodeSystemConcept(
        {
            "code": "old",
            "definition": "The identifier id no longer considered valid, but may be relevant for search purposes.  E.g. Changes to identifier schemes, account merges, etc.",
            "display": "Old",
        }
    )
    """
    Old

    The identifier id no longer considered valid, but may be relevant for search purposes.  E.g. Changes to identifier schemes, account merges, etc.
    """

    class Meta:
        resource = _resource
