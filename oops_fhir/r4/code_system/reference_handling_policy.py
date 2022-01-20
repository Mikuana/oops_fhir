from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ReferenceHandlingPolicy"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ReferenceHandlingPolicy:
    """
    ReferenceHandlingPolicy

    A set of flags that defines how references are supported.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/reference-handling-policy
    """

    literal = CodeSystemConcept(
        {
            "code": "literal",
            "definition": "The server supports and populates Literal references (i.e. using Reference.reference) where they are known (this code does not guarantee that all references are literal; see 'enforced').",
            "display": "Literal References",
        }
    )
    """
    Literal References

    The server supports and populates Literal references (i.e. using Reference.reference) where they are known (this code does not guarantee that all references are literal; see 'enforced').
    """

    logical = CodeSystemConcept(
        {
            "code": "logical",
            "definition": "The server allows logical references (i.e. using Reference.identifier).",
            "display": "Logical References",
        }
    )
    """
    Logical References

    The server allows logical references (i.e. using Reference.identifier).
    """

    resolves = CodeSystemConcept(
        {
            "code": "resolves",
            "definition": "The server will attempt to resolve logical references to literal references - i.e. converting Reference.identifier to Reference.reference (if resolution fails, the server may still accept resources; see logical).",
            "display": "Resolves References",
        }
    )
    """
    Resolves References

    The server will attempt to resolve logical references to literal references - i.e. converting Reference.identifier to Reference.reference (if resolution fails, the server may still accept resources; see logical).
    """

    enforced = CodeSystemConcept(
        {
            "code": "enforced",
            "definition": "The server enforces that references have integrity - e.g. it ensures that references can always be resolved. This is typically the case for clinical record systems, but often not the case for middleware/proxy systems.",
            "display": "Reference Integrity Enforced",
        }
    )
    """
    Reference Integrity Enforced

    The server enforces that references have integrity - e.g. it ensures that references can always be resolved. This is typically the case for clinical record systems, but often not the case for middleware/proxy systems.
    """

    local = CodeSystemConcept(
        {
            "code": "local",
            "definition": "The server does not support references that point to other servers.",
            "display": "Local References Only",
        }
    )
    """
    Local References Only

    The server does not support references that point to other servers.
    """

    class Meta:
        resource = _resource
