from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AlternativeCodeKind"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AlternativeCodeKind:
    """
    AlternativeCodeKind

    Indicates the type of use for which the code is defined.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/codesystem-altcode-kind
    """

    alternate = CodeSystemConcept(
        {
            "code": "alternate",
            "definition": "The code is an alternative code that can be used in any of the circumstances that the primary code can be used.",
            "display": "Alternate Code",
        }
    )
    """
    Alternate Code

    The code is an alternative code that can be used in any of the circumstances that the primary code can be used.
    """

    deprecated = CodeSystemConcept(
        {
            "code": "deprecated",
            "definition": "The code should no longer be used, but was used in the past.",
            "display": "Deprecated",
        }
    )
    """
    Deprecated

    The code should no longer be used, but was used in the past.
    """

    case_insensitive = CodeSystemConcept(
        {
            "code": "case-insensitive",
            "definition": "The code is an alternative to be used when a case insensitive code is required (when the primary codes are case sensitive).",
            "display": "Case Insensitive",
        }
    )
    """
    Case Insensitive

    The code is an alternative to be used when a case insensitive code is required (when the primary codes are case sensitive).
    """

    case_sensitive = CodeSystemConcept(
        {
            "code": "case-sensitive",
            "definition": "The code is an alternative to be used when a case sensitive code is required (when the primary codes are case insensitive).",
            "display": "Case Sensitive",
        }
    )
    """
    Case Sensitive

    The code is an alternative to be used when a case sensitive code is required (when the primary codes are case insensitive).
    """

    expression = CodeSystemConcept(
        {
            "code": "expression",
            "definition": "The code is an alternative for the primary code that is built using the expression grammar defined by the code system.",
            "display": "Expression",
        }
    )
    """
    Expression

    The code is an alternative for the primary code that is built using the expression grammar defined by the code system.
    """

    class Meta:
        resource = _resource
