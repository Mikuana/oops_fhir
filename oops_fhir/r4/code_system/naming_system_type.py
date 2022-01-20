from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["NamingSystemType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class NamingSystemType:
    """
    NamingSystemType

    Identifies the purpose of the naming system.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/namingsystem-type
    """

    codesystem = CodeSystemConcept(
        {
            "code": "codesystem",
            "definition": "The naming system is used to define concepts and symbols to represent those concepts; e.g. UCUM, LOINC, NDC code, local lab codes, etc.",
            "display": "Code System",
        }
    )
    """
    Code System

    The naming system is used to define concepts and symbols to represent those concepts; e.g. UCUM, LOINC, NDC code, local lab codes, etc.
    """

    identifier = CodeSystemConcept(
        {
            "code": "identifier",
            "definition": "The naming system is used to manage identifiers (e.g. license numbers, order numbers, etc.).",
            "display": "Identifier",
        }
    )
    """
    Identifier

    The naming system is used to manage identifiers (e.g. license numbers, order numbers, etc.).
    """

    root = CodeSystemConcept(
        {
            "code": "root",
            "definition": "The naming system is used as the root for other identifiers and naming systems.",
            "display": "Root",
        }
    )
    """
    Root

    The naming system is used as the root for other identifiers and naming systems.
    """

    class Meta:
        resource = _resource
