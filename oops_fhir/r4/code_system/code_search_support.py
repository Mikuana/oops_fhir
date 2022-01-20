from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CodeSearchSupport"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CodeSearchSupport:
    """
    CodeSearchSupport

    The degree to which the server supports the code search parameter on
ValueSet, if it is supported.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/code-search-support
    """

    explicit = CodeSystemConcept(
        {
            "code": "explicit",
            "definition": "The search for code on ValueSet only includes codes explicitly detailed on includes or expansions.",
            "display": "Explicit Codes",
        }
    )
    """
    Explicit Codes

    The search for code on ValueSet only includes codes explicitly detailed on includes or expansions.
    """

    all_ = CodeSystemConcept(
        {
            "code": "all",
            "definition": "The search for code on ValueSet only includes all codes based on the expansion of the value set.",
            "display": "Implicit Codes",
        }
    )
    """
    Implicit Codes

    The search for code on ValueSet only includes all codes based on the expansion of the value set.
    """

    class Meta:
        resource = _resource
